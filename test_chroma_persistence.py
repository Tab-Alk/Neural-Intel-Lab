import os
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

KNOWLEDGE_BASE_DIR = 'knowledge_base'
persist_directory = os.path.abspath("./db")
collection_name = "my_knowledge_base"
model_name = "sentence-transformers/all-MiniLM-L6-v2"

embedding_function = HuggingFaceEmbeddings(model_name=model_name)

if os.path.exists(persist_directory) and os.listdir(persist_directory):
    print("✅ Loading existing vector database...")
    vectordb = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding_function,
        collection_name=collection_name,
    )
else:
    print("🚀 Creating new vector database...")
    loader = DirectoryLoader(
        "knowledge_base",
        glob="**/*.md",
        loader_cls=UnstructuredMarkdownLoader
    )
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    splits = splitter.split_documents(documents)
    vectordb = Chroma.from_documents(
        documents=splits,
        embedding=embedding_function,
        persist_directory=persist_directory,
        collection_name=collection_name,
    )
    print("✅ Vector database created and persisted.")

print(f"DB directory contents: {os.listdir(persist_directory) if os.path.exists(persist_directory) else 'DB dir does not exist!'}")
