# core_engine.py
import logging
import os
import re
import traceback
from typing import List, Tuple, Optional

# Set up logging instead of print statements
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_sqlite_patch():
    """Apply pysqlite3 patch if needed"""
    try:
        __import__('pysqlite3')
        import sys
        sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
        logger.info("Applied pysqlite3 patch successfully")
    except ModuleNotFoundError:
        logger.info("pysqlite3 not found, using default sqlite3")

def safe_import_dependencies():
    """Safely import all dependencies with error handling"""
    try:
        from langchain_chroma import Chroma
        from langchain_community.document_loaders import JSONLoader
        from langchain.text_splitter import RecursiveCharacterTextSplitter
        from langchain_core.documents import Document as LangchainDocument
        from langchain_huggingface import HuggingFaceEmbeddings
        from langchain_groq import ChatGroq
        from langchain_core.prompts import ChatPromptTemplate
        from langchain_core.output_parsers import StrOutputParser
        
        logger.info("All dependencies imported successfully")
        return {
            'Chroma': Chroma,
            'JSONLoader': JSONLoader,
            'RecursiveCharacterTextSplitter': RecursiveCharacterTextSplitter,
            'LangchainDocument': LangchainDocument,
            'HuggingFaceEmbeddings': HuggingFaceEmbeddings,
            'ChatGroq': ChatGroq,
            'ChatPromptTemplate': ChatPromptTemplate,
            'StrOutputParser': StrOutputParser
        }
    except ImportError as e:
        logger.error(f"Failed to import dependencies: {e}")
        raise

# Initialize the patch and imports
setup_sqlite_patch()
deps = safe_import_dependencies()

# Constants
KNOWLEDGE_BASE_DIR = 'knowledge_base'
DB_DIR = 'db'

def get_embedding_function():
    """Gets the embedding function."""
    try:
        return deps['HuggingFaceEmbeddings'](model_name="all-MiniLM-L6-v2")
    except Exception as e:
        logger.error(f"Failed to create embedding function: {e}")
        raise

def check_db_exists() -> bool:
    """Check if ChromaDB files exist"""
    try:
        if not os.path.exists(DB_DIR):
            logger.info(f"Database directory {DB_DIR} does not exist")
            return False
        
        db_files = os.listdir(DB_DIR)
        logger.info(f"Files in {DB_DIR}: {db_files}")
        
        # Look for any ChromaDB-related files
        chroma_indicators = [
            lambda f: f.endswith('.parquet'),
            lambda f: f.endswith('.sqlite3'),
            lambda f: f == 'index',
            lambda f: f.startswith('chroma'),
            lambda f: f.endswith('.json')
        ]
        
        has_db_files = any(
            indicator(f) for f in db_files for indicator in chroma_indicators
        )
        
        logger.info(f"Database files found: {has_db_files}")
        return has_db_files
        
    except Exception as e:
        logger.error(f"Error checking database directory: {e}")
        return False

def build_database_from_jsonl() -> object:
    """Build database from JSONL file"""
    file_path = os.path.join(KNOWLEDGE_BASE_DIR, 'neural_lab_kb.jsonl')
    
    if not os.path.exists(file_path):
        error_msg = f"Knowledge base JSONL file not found: {file_path}"
        logger.error(error_msg)
        raise FileNotFoundError(error_msg)
    
    try:
        logger.info(f"Loading documents from {file_path}")
        loader = deps['JSONLoader'](
            file_path=file_path, 
            jq_schema='.', 
            content_key="text", 
            json_lines=True
        )
        documents = loader.load()
        logger.info(f"Loaded {len(documents)} documents from JSONL")
        
        if not documents:
            raise ValueError("No documents were loaded from the JSONL file")
        
        # Test a few documents
        for i, doc in enumerate(documents[:3]):
            logger.info(f"Document {i}: {len(doc.page_content)} chars, metadata: {doc.metadata}")
        
        embedding_function = get_embedding_function()
        
        # Ensure the directory exists and is writable
        os.makedirs(DB_DIR, exist_ok=True)
        
        # Test if we can write to the directory
        test_file = os.path.join(DB_DIR, 'test_write.txt')
        try:
            with open(test_file, 'w') as f:
                f.write('test')
            os.remove(test_file)
            logger.info(f"Directory {DB_DIR} is writable")
        except Exception as e:
            logger.error(f"Cannot write to directory {DB_DIR}: {e}")
            raise
        
        logger.info(f"Creating ChromaDB in {DB_DIR}")
        db = deps['Chroma'].from_documents(
            documents, 
            embedding_function=embedding_function, 
            persist_directory=DB_DIR
        )
        logger.info("Vector database built successfully")
        
        # Verify the database was created
        if check_db_exists():
            logger.info("Database creation verified")
        else:
            logger.warning("Database files not found after creation")
        
        return db
        
    except Exception as e:
        logger.error(f"Failed to build database: {e}")
        logger.error(f"Full traceback: {traceback.format_exc()}")
        raise

def load_existing_database() -> object:
    """Load existing ChromaDB"""
    try:
        logger.info(f"Attempting to load database from {DB_DIR}")
        embedding_function = get_embedding_function()
        
        # Try to load the database
        db = deps['Chroma'](
            persist_directory=DB_DIR, 
            embedding_function=embedding_function
        )
        
        # Test the database by trying to get the collection
        try:
            collection = db._collection
            doc_count = collection.count()
            logger.info(f"Database loaded with {doc_count} documents")
        except Exception as e:
            logger.warning(f"Could not verify database contents: {e}")
        
        logger.info("Existing vector database loaded successfully")
        return db
        
    except Exception as e:
        logger.error(f"Failed to load existing database: {e}")
        logger.error(f"Full traceback: {traceback.format_exc()}")
        raise

def get_vector_db() -> object:
    """Gets or creates the vector database."""
    try:
        os.makedirs(DB_DIR, exist_ok=True)
        
        if check_db_exists():
            logger.info("Loading existing vector database")
            return load_existing_database()
        else:
            logger.info("Building new vector database from JSONL")
            return build_database_from_jsonl()
            
    except Exception as e:
        logger.error(f"Failed to get vector database: {e}")
        raise

def query_rag(query_text: str, api_key: str) -> Tuple[str, List]:
    """Query the RAG system with error handling"""
    if not api_key:
        raise ValueError("API key is required")
    
    if not query_text.strip():
        raise ValueError("Query text cannot be empty")
    
    try:
        logger.info(f"Processing query: {query_text[:50]}...")
        
        vector_db = get_vector_db()
        retriever = vector_db.as_retriever(search_kwargs={"k": 10})
        
        # Retrieve documents
        source_docs = retriever.invoke(query_text)
        logger.info(f"Retrieved {len(source_docs)} source documents")
        
        # Combine content
        context_text = "\n\n".join([doc.page_content for doc in source_docs])
        
        # Create prompt
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
        
        prompt = deps['ChatPromptTemplate'].from_template(prompt_template_str)
        llm = deps['ChatGroq'](
            temperature=0.2, 
            model_name="llama3-70b-8192", 
            api_key=api_key
        )
        
        # Generate response
        rag_chain = prompt | llm | deps['StrOutputParser']()
        response = rag_chain.invoke({"context": context_text, "question": query_text})
        
        logger.info("RAG query completed successfully")
        
        # Log retrieved sources
        logger.info("Retrieved Sources:")
        for i, doc in enumerate(source_docs):
            logger.info(f"[{i}] Source: {doc.metadata.get('source', 'Unknown')}")
            logger.info(f"Title: {doc.metadata.get('title', 'No title')}")
            logger.info(f"Excerpt: {doc.page_content[:300]}")
        
        return response, source_docs
        
    except Exception as e:
        logger.error(f"Failed to process RAG query: {e}")
        raise

def generate_related_questions(query: str, answer: str, api_key: str) -> List[str]:
    """
    Generates relevant follow-up questions based on the query and answer.
    """
    if not api_key:
        raise ValueError("API key is required")
    
    try:
        prompt_template_str = """
        You are a helpful AI assistant. Your task is to generate insightful follow-up questions based on a user's query and the answer they received.

        Analyze the provided query and answer. Brainstorm 3 to 5 relevant questions that would allow a user to explore the topic further. The questions should be distinct from the original query and encourage deeper investigation into related concepts.

        IMPORTANT: Your output MUST be ONLY a numbered list of the questions, with each question on a new line. Do not include any introductory text, concluding remarks, or any other text besides the questions themselves.

        EXAMPLE OUTPUT:
        1. What are the ethical implications of Hebbian learning in autonomous AI?
        2. How is synaptic plasticity modeled in modern neural networks?
        3. Can an AI without Hebbian-style learning ever achieve true generalization?

        ---
        USER QUERY: {query}
        ---
        ANSWER PROVIDED: {answer}
        ---
        
        YOUR GENERATED FOLLOW-UP QUESTIONS (numbered list only):
        """
        
        prompt = deps['ChatPromptTemplate'].from_template(prompt_template_str)
        llm = deps['ChatGroq'](
            temperature=0.7, 
            model_name="llama3-8b-8192", 
            api_key=api_key
        )
        
        question_generation_chain = prompt | llm | deps['StrOutputParser']()
        response_text = question_generation_chain.invoke({"query": query, "answer": answer})
        
        # Parse questions
        questions = []
        potential_questions = response_text.strip().split('\n')
        for line in potential_questions:
            clean_line = line.strip()
            question_text = re.sub(r'^\d+\.\s*', '', clean_line)
            if question_text:
                questions.append(question_text)
        
        logger.info(f"Generated {len(questions)} related questions")
        return questions
        
    except Exception as e:
        logger.error(f"Failed to generate related questions: {e}")
        return []  # Return empty list instead of raising

def health_check() -> dict:
    """Perform a health check of the system"""
    status = {
        "dependencies": False,
        "knowledge_base": False,
        "database": False,
        "embeddings": False
    }
    
    try:
        # Check dependencies
        if all(key in deps for key in ['Chroma', 'JSONLoader', 'HuggingFaceEmbeddings']):
            status["dependencies"] = True
        
        # Check knowledge base file
        kb_file = os.path.join(KNOWLEDGE_BASE_DIR, 'neural_lab_kb.jsonl')
        if os.path.exists(kb_file):
            status["knowledge_base"] = True
            logger.info(f"Knowledge base file found: {kb_file}")
        else:
            logger.error(f"Knowledge base file not found: {kb_file}")
        
        # Check embeddings first (needed for database)
        try:
            embedding_function = get_embedding_function()
            if embedding_function:
                status["embeddings"] = True
                logger.info("Embeddings function created successfully")
        except Exception as e:
            logger.error(f"Failed to create embeddings function: {e}")
        
        # Check database (most complex check)
        if status["embeddings"] and status["knowledge_base"]:
            try:
                # Try to get the vector database
                db = get_vector_db()
                if db:
                    status["database"] = True
                    logger.info("Database check passed")
            except Exception as e:
                logger.error(f"Database check failed: {e}")
                logger.error(f"Database error traceback: {traceback.format_exc()}")
        else:
            logger.info("Skipping database check due to missing prerequisites")
            
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        logger.error(f"Health check traceback: {traceback.format_exc()}")
    
    return status