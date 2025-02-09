# Question-Answering-QA-System
Small Language Model (SLM)-based Question Answering (QA) System

🚀 Project Overview

This project implements a Small Language Model (SLM)-based Question Answering (QA) System that can take a PDF document as input and accurately answer user queries based on its content. The system is built using FAISS for retrieval and a pretrained transformer model for answer extraction.

✅ Features

PDF-based QA: Users can upload a PDF and ask questions about its content.

Efficient Retrieval: FAISS is used to store and fetch relevant text passages.

Accurate Answering: A fine-tuned question-answering model extracts precise answers.

Web UI: Built with FastAPI (backend) + Streamlit (frontend) for an interactive experience.

Multi-question support: Users can ask multiple questions in one session.

🔥 How It Works

Upload a PDF in the Streamlit UI.

The text is preprocessed and indexed using FAISS.

Users enter a question related to the PDF content.

The FAISS retriever fetches the most relevant passage.

A pretrained Transformer QA model extracts the answer.

The final answer is displayed in the UI.

📖 My Approach

The development of this SLM-based QA system follows a structured pipeline:

PDF Preprocessing:

Extract text from PDF files using PyMuPDF.

Clean and segment the extracted text into logical passages to improve retrieval accuracy.

Passage Retrieval (FAISS):

Use sentence embeddings generated via all-MiniLM-L6-v2.

Store embeddings in a FAISS index for efficient similarity-based search.

Retrieve the most relevant passage for a given user question.

Answer Extraction (Transformer Model):

Utilize distilbert-base-cased-distilled-squad for extractive question-answering.

Process the retrieved passage + user question through the transformer model.

Identify and return the most probable answer using start-end token prediction.

User Interface:

Provide an interactive UI using Streamlit.

Enable users to upload PDFs, ask multiple questions, and view results dynamically.

This approach ensures a fast, accurate, and scalable QA system while keeping it lightweight and efficient.
