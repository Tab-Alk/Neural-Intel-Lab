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
                            st.markdown(f"- Title: {doc.metadata