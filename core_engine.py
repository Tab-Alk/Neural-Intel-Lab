# core_engine.py (Final Verified Version with Caching & Telemetry Fixes)

# Conditional patch for pysqlite3
try:
    __import__('pysqlite3')
    import sys
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except ModuleNotFoundError:
    pass

import os
import re
import streamlit as st # ADDED: For caching decorator
from langchain_community.document_loaders import JSONLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from chromadb.config import Settings # ADDED: To configure and disable ChromaDB telemetry

KNOWLEDGE_BASE_DIR = 'knowledge_base'
DB_DIR = 'db'

# MODIFIED: Added the @st.cache_resource decorator
@st.cache_resource
def get_embedding_function():
    """Gets the embedding function and caches it across user sessions."""
    print("Loading embedding model... (This will only run once per session)")
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# MODIFIED: Added client_settings to disable telemetry
def get_vector_db():
    """Loads or builds the Chroma vector database with telemetry disabled."""
    # ADDED: Define settings to disable telemetry
    client_settings = Settings(anonymized_telemetry=False)
    
    embedding_function = get_embedding_function()
    
    if not os.path.exists(DB_DIR) or not os.listdir(DB_DIR):
        print("Database not found or empty. Building now from .jsonl file...")
        file_path = os.path.join(KNOWLEDGE_BASE_DIR, 'neural_lab_kb.jsonl')
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Knowledge base file not found at {file_path}. Cannot build database.")
        
        loader = JSONLoader(file_path=file_path, jq_schema='.', content_key="text", json_lines=True)
        documents = loader.load()
        
        # ADDED: Pass the settings when creating the DB
        db = Chroma.from_documents(documents, embedding_function, persist_directory=DB_DIR, client_settings=client_settings)
        print("Vector database setup complete.")
    else:
        print("Loading existing vector database.")
        # ADDED: Pass the settings when loading the DB
        db = Chroma(persist_directory=DB_DIR, embedding_function=embedding_function, client_settings=client_settings)
    return db

def query_rag(query_text: str, api_key: str):
    """
    Queries the RAG pipeline using the improved logic.
    """
    vector_db = get_vector_db()
    retriever = vector_db.as_retriever(search_kwargs={"k": 5})
    
    source_docs = retriever.invoke(query_text)
    context_text = "\n\n".join([doc.page_content for doc in source_docs])
    
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
    response = rag_chain.invoke({"context": context_text, "question": query_text})

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