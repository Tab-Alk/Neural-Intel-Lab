# core_engine.py

print("DEBUG: core_engine.py - Script started at top of file.") # Keep this print



# (The conditional patch for pysqlite3 remains commented out as per previous step)

# try:

#     __import__('pysqlite3')

#     import sys

#     sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

# except ModuleNotFoundError:

#     pass



print("DEBUG: core_engine.py - After pysqlite3 patch block (whether active or commented).") # Keep this print



# COMMENT OUT THIS LINE: from llama_parse import LlamaParse

# from llama_parse import LlamaParse



from langchain_chroma import Chroma

print("DEBUG: core_engine.py - After langchain_chroma import.") # THIS IS THE CRUCIAL PRINT



import os

import re

from langchain_community.document_loaders import JSONLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_core.documents import Document as LangchainDocument

from langchain_huggingface import HuggingFaceEmbeddings

# from langchain_chroma import Chroma # This line is duplicated, one is enough

from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

print("DEBUG: core_engine.py - After all core imports (os, re, langchain, etc.).") # Keep this print



KNOWLEDGE_BASE_DIR = 'knowledge_base'

DB_DIR = 'db' # Keep this as 'db' so it tries to create it there



def get_embedding_function():

    """Gets the embedding function."""

    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")



def get_vector_db():

    embedding_function = get_embedding_function()

    

    # Ensure DB_DIR is created if it doesn't exist. This is important for Chroma to persist.

    os.makedirs(DB_DIR, exist_ok=True) 



    # Check if DB_DIR actually contains ChromaDB files (e.g., 'chroma-embeddings.parquet')

    # This is a more robust check than just os.path.exists(DB_DIR)

    db_files_exist = False

    if os.path.exists(DB_DIR):

        # Look for a common file that Chroma creates for persistence

        if any(f.endswith('.parquet') for f in os.listdir(DB_DIR)) or any(d == 'index' for d in os.listdir(DB_DIR)):

             db_files_exist = True



    if not db_files_exist:

        print("DEBUG: get_vector_db - Database not found or empty. Attempting to BUILD from .jsonl file...")

        file_path = os.path.join(KNOWLEDGE_BASE_DIR, 'neural_lab_kb.jsonl')

        if not os.path.exists(file_path):

            print(f"ERROR: {file_path} not found. Cannot build database. Please ensure 'knowledge_base/neural_lab_kb.jsonl' is in your repo and tracked.")

            # We must raise an error here, otherwise the app will fail later trying to query an empty DB

            raise FileNotFoundError(f"Knowledge base JSONL file not found: {file_path}")



        loader = JSONLoader(file_path=file_path, jq_schema='.', content_key="text", json_lines=True)

        documents = loader.load()

        text_chunks = documents 

        print("DEBUG: get_vector_db - Calling Chroma.from_documents to build NEW DB.")

        db = Chroma.from_documents(text_chunks, embedding_function, persist_directory=DB_DIR)

        print("DEBUG: get_vector_db - Vector database setup complete (NEW DB built).")

    else:

        print("DEBUG: get_vector_db - LOADING existing vector database from disk.")

        db = Chroma(persist_directory=DB_DIR, embedding_function=embedding_function)

        print("DEBUG: get_vector_db - Vector database LOADED.")



    print("DEBUG: core_engine.py - After get_vector_db setup completed.") # Keep this print

    return db



# ... rest of your core_engine.py code (query_rag, generate_related_questions, commented out LlamaParse functions)