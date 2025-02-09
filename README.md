# Question-Answering-QA-System
Small Language Model (SLM)-based Question Answering (QA) System

🚀 Project Overview

This project implements a Small Language Model (SLM)-based Question Answering (QA) System that can take a PDF document as input and accurately answer user queries based on its content. The system is built using FAISS for retrieval and a pretrained transformer model for answer extraction.

✅ Features

- PDF-based QA: Users can upload a PDF and ask questions about its content.
- Efficient Retrieval: FAISS is used to store and fetch relevant text passages.
- Accurate Answering: A fine-tuned question-answering model extracts precise answers.
- Web UI: Built with FastAPI (backend) + Streamlit (frontend) for an interactive experience.
- Multi-question support: Users can ask multiple questions in one session.

🛠️ Setup & Installation

1. Clone the Repository: 
git clone https://github.com/yourusername/Question-Answering-QA-System.git
cd Question-Answering-QA-System

2. Install Dependencies:
pip install -r requirements.txt
  
3. Run the Backend (FastAPI):
uvicorn app.main:app --reload
   
4. Run the UI (Streamlit):
streamlit run app/ui.py

5. Access the Application:
The FastAPI backend will be available at: http://127.0.0.1:8000.
The Streamlit frontend will be available at: http://localhost:8501.

🔥 How It Works

1. Upload a PDF in the Streamlit UI.
2. The text is preprocessed and indexed using FAISS.
3. Users enter a question related to the PDF content.
4. The FAISS retriever fetches the most relevant passage.
5. A pretrained Transformer QA model extracts the answer.
6. The final answer is displayed in the UI.

📖 My Approach

The development of this SLM-based QA system follows a structured pipeline:

1. PDF Preprocessing:
- Extract text from PDF files using PyMuPDF.
- Clean and segment the extracted text into logical passages to improve retrieval accuracy.

2. Passage Retrieval (FAISS):
- Use sentence embeddings generated via all-MiniLM-L6-v2.
- Store embeddings in a FAISS index for efficient similarity-based search.
- Retrieve the most relevant passage for a given user question.

3. Answer Extraction (Transformer Model):
- Utilize distilbert-base-cased-distilled-squad for extractive question-answering.
- Process the retrieved passage + user question through the transformer model.
- Identify and return the most probable answer using start-end token prediction.

4. User Interface:
- Provide an interactive UI using Streamlit.
- Enable users to upload PDFs, ask multiple questions, and view results dynamically.

This approach ensures a fast, accurate, and scalable QA system while keeping it lightweight and efficient.

🏗️ Model Architecture
1. Preprocessing (Text Extraction & Cleaning)
- Library Used: PyMuPDF
- Process:
  1. Extracts raw text from PDFs.
  2. Removes unwanted whitespace, special characters, and noisy data.
  3. Splits text into smaller meaningful chunks for indexing.
     
2. Retrieval (FAISS + Sentence Embeddings)
- Library Used: FAISS, all-MiniLM-L6-v2
- Process:
  1. Converts PDF text into sentence embeddings.
  2. Stores embeddings in a FAISS vector index.
  3. Retrieves the most relevant passage for a given user question.
     
3. Answer Extraction (QA Transformer Model)
- Model Used: distilbert-base-cased-distilled-squad
- Process:
  1. The retrieved passage + user question are tokenized.
  2. The model predicts start and end positions of the answer.
  3. The best possible answer is extracted and returned.
 
📊 Evaluation & Key Learnings

1. Challenges Faced
- Some answers were irrelevant because FAISS retrieved incorrect passages.
- Text extraction from PDFs sometimes included noisy data.

2. Improvements & Fixes
- Switched to paragraph-based FAISS indexing for better retrieval.
- Added answer validation to avoid returning incorrect words.
- Applied text cleaning techniques to improve document structure.

3. Future Enhancements
- Implement LLM-powered Retrieval-Augmented Generation (RAG).
- Add OCR support for scanned PDFs.
- Improve answer ranking using confidence scores.

