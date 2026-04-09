# DocumentIQ: RAG Chatbot

DocumentIQ is a sophisticated Retrieval-Augmented Generation (RAG) chatbot designed to provide intelligent answers based on your own documents. It leverages advanced NLP models and vector databases to deliver accurate, context-aware responses.

## 🚀 Features

- **Multi-Document Support**: Upload and index PDFs, Word documents, and text files.
- **RAG-Powered Conversations**: Uses Retrieval-Augmented Generation to ground AI responses in your specific data.
- **Audio Support**: Integrated speech recognition for voice-enabled queries.
- **Interactive UI**: A clean, modern Streamlit interface for seamless user interaction.
- **Hybrid Storage**: Combines MongoDB for metadata and ChromaDB for high-performance vector search.
- **Scalable Backend**: Powered by FastAPI for robust and efficient API handling.

## 🛠️ Technology Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Orchestration**: [LangChain](https://www.langchain.com/)
- **LLM**: Google Gemini (via `langchain-google-genai`)
- **Vector Database**: [ChromaDB](https://www.trychroma.com/)
- **Metadata Database**: [MongoDB](https://www.mongodb.com/)
- **Embeddings**: HuggingFace / Sentence Transformers
- **Document Parsing**: PyPDF, docx2txt, Unstructured

## 📋 Prerequisites

- Python 3.9+
- MongoDB instance (Local or Atlas)
- Google Gemini API Key

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/DocumentIQ-RAG-Chatbot.git
cd DocumentIQ-RAG-Chatbot
```

### 2. Configure Environment Variables
Navigate to the `Chatbot` directory and create a `.env` file based on the provided template:
```bash
cd Chatbot
cp .env.example .env
```
Edit `.env` and fill in your credentials:
- `DB_URI`: Your MongoDB connection string.
- `GEMINI_API_KEY`: Your Google Gemini API key.

### 3. Install Dependencies
It is recommended to use a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 🏃 Running the Application

DocumentIQ consists of two main components: the FastAPI backend and the Streamlit frontend.

### 1. Start the Backend API
```bash
python src/main.py
```
*The API will typically run on http://localhost:8000*

### 2. Launch the Streamlit Frontend
In a new terminal:
```bash
streamlit run src/streamlit_app.py
```

## 📂 Project Structure

- `Chatbot/src/`: Core source code (API, RAG logic, UI).
- `Chatbot/data/`: Local storage for vector embeddings and document cache.
- `Chatbot/Images/`: UI assets and logos.
- `render.yaml`: Deployment configuration for Render.
