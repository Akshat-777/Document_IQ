import streamlit as st
from src.api_utils import upload_document, list_documents

def display_sidebar():
    # Model & Networking info
    from src.api_utils import API_URL
    st.sidebar.markdown(f"**Model:** `llama-3.3-70b-versatile`\n\n**API URL:** `{API_URL}`")

    # Document upload
    uploaded_file = st.sidebar.file_uploader("Choose a file", type=["pdf", "docx", "html"])
    if uploaded_file and st.sidebar.button("Upload"):
        with st.spinner("Uploading..."):
            upload_response = upload_document(uploaded_file)
            if upload_response:
                st.sidebar.success(f"File uploaded successfully with ID {upload_response['file_id']}.")