# core_engine.py (Final Verified Version with Caching & Telemetry Fixes)

# Conditional patch for pysqlite3
try:
    import pysqlite3
    import sys
    sys.modules["sqlite3"] = pysqlite3
except ImportError:
    pass  # fallback to system sqlite3 if pysqlite3 is not available

import os
import logging
logging.basicConfig(level=logging.INFO)
import re
import time
import streamlit as st # ADDED: For caching decorator
from langchain_community.document_loaders import JSONLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader

persist_directory = os.path.abspath("./db")
collection_name = "my_knowledge_base"
model_name = "sentence-transformers/all-MiniLM-L6-v2"
KNOWLEDGE_BASE_DIR = 'knowledge_base'

@st.cache_resource
def get_embedding_function():
    """Gets the embedding function and caches it across user sessions."""
    print("Loading embedding model... (This will only run once per session)")
    return HuggingFaceEmbeddings(model_name=model_name)

def get_vector_db():
    """
    Loads or builds the Chroma vector database using the new Chroma client pattern.
    
    Returns:
        Chroma: Initialized Chroma vector database instance.
    """
    import chromadb
    from chromadb.config import Settings
    
    # Initialize embedding function
    embedding_function = get_embedding_function()
    
    try:
        # Create directory if it doesn't exist
        os.makedirs(persist_directory, exist_ok=True)
        
        # Initialize Chroma client with the new PersistentClient
        client = chromadb.PersistentClient(path=persist_directory)
        
        # Check if the collection exists
        try:
            collection_list = client.list_collections()
            collection_exists = any(collection.name == collection_name for collection in collection_list)
            
            if collection_exists:
                logging.info(f"✅ Found existing collection: {collection_name}")
                # Create LangChain Chroma instance with the existing collection
                vectordb = Chroma(
                    client=client,
                    collection_name=collection_name,
                    embedding_function=embedding_function,
                )
                # Test the connection
                _ = vectordb._collection.count()
                logging.info("✅ Successfully loaded existing vector database.")
                return vectordb
                
        except Exception as e:
            logging.warning(f"⚠️ Could not access existing collection: {str(e)}")
            # If we can't access the collection, we'll create a new one
            pass
        
        # If we get here, we need to create a new collection
        logging.info(f"📂 Loading documents from '{KNOWLEDGE_BASE_DIR}'...")
        loader = DirectoryLoader(
            KNOWLEDGE_BASE_DIR,
            glob="**/*.md",
            loader_cls=UnstructuredMarkdownLoader
        )
        documents = loader.load()
        
        if not documents:
            raise FileNotFoundError(
                f"❌ No Markdown (.md) documents found in the '{KNOWLEDGE_BASE_DIR}' directory. "
                "Please add at least one .md file to build the knowledge base."
            )
            
        logging.info(f"📄 Loaded {len(documents)} Markdown documents.")
        
        # Split documents into chunks
        from langchain_text_splitters import RecursiveCharacterTextSplitter
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=100,
            length_function=len,
            add_start_index=True,
        )
        splits = splitter.split_documents(documents)
        logging.info(f"✂️  Split into {len(splits)} chunks.")
        
        # Create new ChromaDB with the new client pattern
        vectordb = Chroma.from_documents(
            documents=splits,
            embedding=embedding_function,
            client=client,
            collection_name=collection_name,
            persist_directory=persist_directory,
        )
        
        logging.info("✅ Vector database created and persisted successfully.")
        return vectordb
        
    except Exception as e:
        logging.error(f"❌ Error initializing vector database: {str(e)}")
        # Clean up if something went wrong
        if os.path.exists(persist_directory):
            import shutil
            shutil.rmtree(persist_directory, ignore_errors=True)
        raise

def query_rag(query_text: str, api_key: str):
    """
    Queries the RAG pipeline using the improved logic.
    """
    print("Starting RAG query...")
    t0 = time.time()
    vector_db = get_vector_db()
    print(f"Loaded vector DB in {time.time() - t0:.2f}s")
    retriever = vector_db.as_retriever(search_kwargs={"k": 3})
    t1 = time.time()
    source_docs = retriever.invoke(query_text)
    print(f"Retrieved context in {time.time() - t1:.2f}s")
    context_text = "\n\n".join([doc.page_content for doc in source_docs])
    # Limit context to 10,000 characters (about 3,000 tokens)
    MAX_CONTEXT_CHARS = 10000
    if len(context_text) > MAX_CONTEXT_CHARS:
        context_text = context_text[:MAX_CONTEXT_CHARS]
    prompt_template_str = """
    You are an expert AI assistant. Your goal is to provide clear, concise, and accurate answers based on the context provided.
    Compare and contrast the concepts from the provided text, focusing on the user's question.
    Do not mention that you are answering from a provided context.
    
    CONTEXT:
    {context}
    
    QUESTION:
    {question}
    
    ANSWER:
    """
    prompt = ChatPromptTemplate.from_template(prompt_template_str)
    llm = ChatGroq(temperature=0.2, model_name="llama3-70b-8192", api_key=api_key)
    
    rag_chain = prompt | llm | StrOutputParser()
    t2 = time.time()
    response = rag_chain.invoke({"context": context_text, "question": query_text})
    print(f"LLM call took {time.time() - t2:.2f}s")

    print("\n--- Retrieved Sources (for debugging) ---")
    for i, doc in enumerate(source_docs):
        source_file = doc.metadata.get('source', 'Unknown')
        title = doc.metadata.get('title', f"From {os.path.basename(source_file)}")
        print(f"[{i}] Title: {title}, Source File: {source_file}")

    return response, source_docs

def generate_related_questions(query: str, answer: str, api_key: str):
    """
    Generates relevant follow-up questions using a more robust and direct prompt.
    """
    prompt_template_str = """
    You are a Question Generation Bot. Your sole purpose is to generate relevant, insightful follow-up questions based on the provided text. You must not do anything else.

    The user asked the following QUESTION:
    "{query}"

    They received this ANSWER:
    "{answer}"

    Based on this information, generate exactly 3 follow-up questions that would allow a user to explore the topic further.

    RULES:
    1. The questions must be distinct from the original query.
    2. The questions must encourage deeper investigation into related concepts.
    3. Your entire response MUST consist ONLY of a numbered list of the questions.
    4. DO NOT provide any commentary, preamble, or ask for clarification. DO NOT write "Here are some questions:".

    EXAMPLE OUTPUT:
    1. What are the ethical implications of Hebbian learning in autonomous AI?
    2. How is synaptic plasticity modeled in modern neural networks?
    3. Can an AI without Hebbian-style learning ever achieve true generalization?

    YOUR GENERATED FOLLOW-UP QUESTIONS (numbered list only):
    """
    prompt = ChatPromptTemplate.from_template(prompt_template_str)
    
    llm = ChatGroq(temperature=0.7, model_name="llama3-8b-8192", api_key=api_key)
    
    question_generation_chain = prompt | llm | StrOutputParser()
    response_text = question_generation_chain.invoke({"query": query, "answer": answer})
    
    questions = []
    potential_questions = response_text.strip().split('\n')
    for line in potential_questions:
        clean_line = line.strip()
        question_text = re.sub(r'^\d+\.\s*', '', clean_line)
        if question_text:
            questions.append(question_text)
            
    return questions