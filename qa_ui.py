import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("📖 PDF Question Answering")
uploaded_file = st.file_uploader("📂 Upload a PDF", type=["pdf"])

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("✅ PDF uploaded!")

    requests.post(f"{API_URL}/upload_pdf/", files={"file": open("temp.pdf", "rb")})

question = st.text_input("❓ Ask a question:")
if st.button("Get Answer"):
    response = requests.post(f"{API_URL}/answer/", json={"question": question})
    st.write(f"✅ **Answer:** {response.json().get('answer', 'No answer found.')}")
