# core_engine.py (Definitive "Golden State" Version)

# Conditional patch for pysqlite3
try:
    __import__('pysqlite3')
    import sys
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except ModuleNotFoundError:
    pass

import os
import re
from langchain_community.document_loaders import JSONLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

KNOWLEDGE_BASE_DIR = 'knowledge_base'
DB_DIR = 'db'

def get_embedding_function():
    """Gets the embedding function."""
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def get_vector_db():
    """Loads or builds the Chroma vector database."""
    embedding_function = get_embedding_function()
    if not os.path.exists(DB_DIR) or not os.listdir(DB_DIR):
        print("Database not found or empty. Building now from .jsonl file...")
        file_path = os.path.join(KNOWLEDGE_BASE_DIR, 'neural_lab_kb.jsonl')
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Knowledge base file not found at {file_path}. Cannot build database.")
        
        loader = JSONLoader(file_path=file_path, jq_schema='.', content_key="text", json_lines=True)
        documents = loader.load()
        
        db = Chroma.from_documents(documents, embedding_function, persist_directory=DB_DIR)
        print("Vector database setup complete.")
    else:
        print("Loading existing vector database.")
        db = Chroma(persist_directory=DB_DIR, embedding_function=embedding_function)
    return db

def query_rag(query_text: str, api_key: str):
    """
    Queries the RAG pipeline using the improved logic.
    """
    vector_db = get_vector_db()
    retriever = vector_db.as_retriever(search_kwargs={"k": 5}) # Using k=5 as requested
    
    source_docs = retriever.invoke(query_text)
    context_text = "\n\n".join([doc.page_content for doc in source_docs])
    
    prompt_template_str = """
    You are an expert AI assistant...
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
    Generates relevant follow-up questions...
    """
    # This function's logic is sound, no changes needed from your version.
    prompt_template_str = """
    You are a helpful AI assistant...
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