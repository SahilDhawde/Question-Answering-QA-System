from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import fitz  
from sentence_transformers import SentenceTransformer
import faiss
import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

app = FastAPI()
sentence_model = SentenceTransformer("all-MiniLM-L6-v2")
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-cased-distilled-squad")
model = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-cased-distilled-squad")

INDEX = None
PASSAGES = []

def extract_text(pdf_input):
    if isinstance(pdf_input, (str, bytes)):  # If input is a file path or bytes
        doc = fitz.open(pdf_input)
    elif hasattr(pdf_input, "read"):  # If input is a file-like object
        doc = fitz.open("pdf", pdf_input.read())
    else:
        raise ValueError("Invalid input: Provide a file path or file-like object.")
    
    return " ".join([page.get_text("text") for page in doc])

def build_faiss_index(passages):
    passages = "\n\n".join(passages).split("\n\n")
    embeddings = sentence_model.encode(passages, convert_to_numpy=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index, passages

@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    global INDEX, PASSAGES
    pdf_text = extract_text(file.file)
    PASSAGES = pdf_text.split(". ")  # Split into short passages
    INDEX, PASSAGES = build_faiss_index(PASSAGES)
    return {"message": "PDF processed successfully"}

class QuestionRequest(BaseModel):
    question: str

@app.post("/answer/")
def get_answer(request: QuestionRequest):
    global INDEX, PASSAGES
    if INDEX is None:
        return {"error": "No PDF uploaded!"}

    question_embedding = sentence_model.encode([request.question], convert_to_numpy=True)
    _, indices = INDEX.search(question_embedding, 1)
    best_passage = PASSAGES[indices[0][0]]

    inputs = tokenizer(request.question, best_passage, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)


    start, end = torch.argmax(outputs.start_logits), torch.argmax(outputs.end_logits)
    if start > end:
        answer = "No relevant answer found."
    else:
        answer = tokenizer.convert_tokens_to_string(
            tokenizer.convert_ids_to_tokens(inputs.input_ids[0][start:end+1])
        )

    return {"answer": answer}

print("Done")