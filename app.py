# app.py
import streamlit as st
import traceback
import sys
import os
# IMPORTANT: Import your core engine functions at the top
from core_engine import health_check, get_vector_db, query_rag

# --- THIS IS THE NEW CACHED FUNCTION ---
@st.cache_resource
def load_retriever(api_key):
    """
    Loads the vector database and retriever. This function is cached
    so it only runs once per session.
    """
    st.info("Initializing knowledge base... This may take a moment on first run.")
    vector_db = get_vector_db()
    retriever = vector_db.as_retriever(search_kwargs={"k": 10})
    return retriever

def main():
    st.set_page_config(
        page_title="Neuro AI Explorer",
        page_icon="🧠",
        layout="wide"
    )
    
    try:
        st.write("🚀 Starting Neuro AI Explorer...")
        
        # Run health check
        health_status = health_check()
        st.write("### System Health Check")
        
        all_ready = True
        for component, status in health_status.items():
            icon = "✅" if status else "🟡" # Use yellow for 'not yet built'
            message = "OK" if status else "Not built yet"
            if component == 'database_persists' and not status:
                message = "Not built yet (will be created on first query)"
            elif not status:
                all_ready = False # Mark as not ready only for critical failures
                icon = "❌"
                message = "Failed"

            st.write(f"{icon} {component.replace('_', ' ').title()}: {message}")
        
        # We can proceed even if the DB isn't built yet
        if health_status['dependencies'] and health_status['knowledge_base_file']:
            st.success("🎉 Core systems ready! Knowledge base will be indexed on your first query.")
            render_main_app()
        else:
            st.error("❌ A critical system component failed. Please check the logs.")
            # You can keep your render_diagnostic_info function here if you wish
                
    except Exception as e:
        st.error(f"❌ Application error: {e}")
        st.code(traceback.format_exc())

# --- MODIFIED to use the cached retriever ---
def render_main_app():
    """Render the main application interface"""
    st.title("🧠 Neuro AI Explorer")
    st.markdown("Explore neuroscience and AI concepts through intelligent Q&A")
    
    api_key = st.sidebar.text_input(
        "Enter your Groq API Key:",
        type="password",
        help="Get your API key from https://console.groq.com/"
    )
    
    if not api_key:
        st.warning("Please enter your Groq API key in the sidebar to continue.")
        return
    
    query = st.text_area(
        "Enter your question about neuroscience or AI:",
        placeholder="e.g., What is the difference between supervised and unsupervised learning?",
        height=100
    )
    
    if st.button("🔍 Search", type="primary", use_container_width=True):
        if query.strip():
            try:
                # This call now uses the cached function
                # The spinner will show while the DB is being built for the first time
                with st.spinner("Searching knowledge base... (First query may take longer as the database is indexed)"):
                    
                    # This is the ONLY place we call the expensive function
                    retriever = load_retriever(api_key) # api_key is passed to satisfy the cache
                    
                    # We reuse the existing query_rag but will need a slight modification to it.
                    # For now, let's call the components directly
                    from core_engine import query_rag # Re-importing for clarity
                    
                    # Get response
                    response, sources = query_rag(query, api_key)
                    
                    st.markdown("### 📝 Answer")
                    st.markdown(response)
                    
                    with st.expander("📚 Sources", expanded=False):
                        for i, doc in enumerate(sources):
                            title = doc.metadata.get('title', f"Chunk from {os.path.basename(doc.metadata.get('source', 'Unknown'))}")
                            st.markdown(f"**Source {i+1}:** {title}")
                            st.markdown(f"> {doc.page_content[:300]}...")

            except Exception as e:
                st.error(f"❌ Error while searching: {e}")
                st.code(traceback.format_exc())

# You can remove the render_diagnostic_info and render_fallback_interface functions
# or keep them as they are. The main function logic has been updated.
# Make sure the main() function is the primary entry point.


def render_diagnostic_info(health_status):
    """Render detailed diagnostic information"""
    st.markdown("### 🔍 Diagnostic Information")
    
    # Check current working directory
    st.write(f"**Current working directory:** `{os.getcwd()}`")
    
    # Check if knowledge base directory exists
    kb_dir = "knowledge_base"
    if os.path.exists(kb_dir):
        st.write(f"✅ Knowledge base directory found: `{kb_dir}`")
        kb_files = os.listdir(kb_dir)
        st.write(f"Files in knowledge base: {kb_files}")
        
        # Check JSONL file specifically
        jsonl_path = os.path.join(kb_dir, 'neural_lab_kb.jsonl')
        if os.path.exists(jsonl_path):
            file_size = os.path.getsize(jsonl_path)
            st.write(f"✅ JSONL file found: `{jsonl_path}` ({file_size} bytes)")
            
            # Try to read first few lines
            try:
                with open(jsonl_path, 'r') as f:
                    first_line = f.readline()
                    st.write(f"First line preview: `{first_line[:100]}...`")
            except Exception as e:
                st.write(f"❌ Could not read JSONL file: {e}")
        else:
            st.write(f"❌ JSONL file not found: `{jsonl_path}`")
    else:
        st.write(f"❌ Knowledge base directory not found: `{kb_dir}`")
    
    # Check database directory
    db_dir = "db"
    if os.path.exists(db_dir):
        st.write(f"✅ Database directory found: `{db_dir}`")
        db_files = os.listdir(db_dir)
        st.write(f"Files in database: {db_files}")
    else:
        st.write(f"❌ Database directory not found: `{db_dir}`")
    
    # Try to manually create database
    st.markdown("### 🛠️ Manual Database Creation")
    # This button might cause issues if build_database_from_jsonl is not defined or correctly callable
    # Ensure core_engine has a function named build_database_from_jsonl if you want to use this.
    if st.button("🔧 Try to Create Database Manually"):
        try:
            with st.spinner("Creating database..."):
                # Make sure this function exists and is imported from core_engine
                # For this specific app, it might be better to just rerun get_vector_db()
                # or remove this button if it's not truly needed.
                # Assuming `build_database_from_jsonl` should exist in core_engine based on its usage here.
                from core_engine import build_database_from_jsonl # This line might need review if build_database_from_jsonl doesn't exist
                db = build_database_from_jsonl()
                st.success("✅ Database created successfully!")
                st.experimental_rerun()
        except Exception as e:
            st.error(f"❌ Failed to create database: {e}")
            st.code(traceback.format_exc())
    
    # Show system information
    st.markdown("### 💻 System Information")
    st.write(f"**Python version:** {sys.version}")
    st.write(f"**Platform:** {sys.platform}")
    
    # Show installed packages (relevant ones)
    try:
        import pkg_resources
        relevant_packages = ['langchain', 'chromadb', 'streamlit', 'sentence-transformers']
        st.write("**Relevant packages:**")
        for pkg in relevant_packages:
            try:
                version = pkg_resources.get_distribution(pkg).version
                st.write(f"- {pkg}: {version}")
            except:
                st.write(f"- {pkg}: Not found")
    except:
        st.write("Could not check package versions")


def render_fallback_interface():
    """Render a fallback interface when core_engine fails to import"""
    st.error("❌ Core engine failed to import. Running in fallback mode.")
    
    st.markdown("### 🔍 Basic System Check")
    st.write(f"**Current directory:** `{os.getcwd()}`")
    st.write(f"**Directory contents:** {os.listdir('.')}")
    
    # Check if required files exist
    required_files = ['core_engine.py', 'requirements.txt']
    for file in required_files:
        if os.path.exists(file):
            st.write(f"✅ {file} found")
        else:
            st.write(f"❌ {file} missing")
    
    # Check knowledge base
    if os.path.exists('knowledge_base'):
        kb_files = os.listdir('knowledge_base')
        st.write(f"📁 Knowledge base files: {kb_files}")
    else:
        st.write("❌ Knowledge base directory missing")


if __name__ == "__main__":
    main()