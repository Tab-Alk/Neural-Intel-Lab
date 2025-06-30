
## app.py
import streamlit as st
import traceback
import sys
import os

# Add error handling for the entire app
def main():
    st.set_page_config(
        page_title="Neuro AI Explorer",
        page_icon="🧠",
        layout="wide"
    )
    
    try:
        # First, let's check if we can import our core engine
        st.write("🚀 Starting Neuro AI Explorer...")
        
        # Try to import core_engine with error handling
        try:
            from core_engine import health_check, query_rag, generate_related_questions
            st.success("✅ Core engine imported successfully!")
            
            # Run health check
            health_status = health_check()
            st.write("### System Health Check")
            
            for component, status in health_status.items():
                icon = "✅" if status else "❌"
                st.write(f"{icon} {component.replace('_', ' ').title()}: {'OK' if status else 'Failed'}")
            
            # Check if all systems are ready
            all_ready = all(health_status.values())
            
            if all_ready:
                st.success("🎉 All systems ready!")
                render_main_app()
            else:
                st.error("❌ Some systems are not ready. Please check the logs.")
                render_diagnostic_info(health_status)
                
        except ImportError as e:
            st.error(f"❌ Failed to import core_engine: {e}")
            st.code(traceback.format_exc())
            render_fallback_interface()
            
    except Exception as e:
        st.error(f"❌ Application error: {e}")
        st.code(traceback.format_exc())


def render_main_app():
    """Render the main application interface"""
    st.title("🧠 Neuro AI Explorer")
    st.markdown("Explore neuroscience and AI concepts through intelligent Q&A")
    
    # API Key input
    api_key = st.sidebar.text_input(
        "Enter your Groq API Key:",
        type="password",
        help="Get your API key from https://console.groq.com/"
    )
    
    if not api_key:
        st.warning("Please enter your Groq API key in the sidebar to continue.")
        return
    
    # Main query interface
    st.markdown("### Ask a Question")
    query = st.text_area(
        "Enter your question about neuroscience or AI:",
        placeholder="e.g., What is the difference between supervised and unsupervised learning?",
        height=100
    )
    
    if st.button("🔍 Search", type="primary", use_container_width=True):
        if query.strip():
            try:
                with st.spinner("Searching knowledge base..."):
                    from core_engine import query_rag, generate_related_questions
                    
                    # Get response
                    response, sources = query_rag(query, api_key)
                    
                    # Display response
                    st.markdown("### 📝 Answer")
                    st.markdown(response)
                    
                    # Display sources
                    with st.expander("📚 Sources", expanded=False):
                        for i, doc in enumerate(sources):
                            st.markdown(f"**Source {i+1}:**")
                            st.markdown(f"- Title: {doc.metadata}")
            except Exception as e:
                st.error(f"❌ Error while searching: {e}")
                st.code(traceback.format_exc())


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
    if st.button("🔧 Try to Create Database Manually"):
        try:
            with st.spinner("Creating database..."):
                from core_engine import build_database_from_jsonl
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
