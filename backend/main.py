from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os
import fitz  # PyMuPDF
import openai  # Correct OpenAI library

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

app = FastAPI()

def extract_text_from_pdf(file_bytes):
    """Extract text from a PDF file."""
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    text = ''
    for page in doc:
        text += page.get_text()
    return text.strip()

@app.post('/upload/')
async def upload_document(
    file: UploadFile = File(...),
    instructions: str = Form("Summarize this legal document")
):
    """Endpoint to upload a legal document and get a summary."""
    contents = await file.read()

    # Extract text based on file type
    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(contents)
    elif file.filename.endswith(".txt"):
        text = contents.decode()
    else:
        return JSONResponse(content={"error": "Unsupported file type"}, status_code=400)

    # Prepare prompt for the LLM
    prompt = f"""
    You are a legal assistant. Analyze the following legal document and provide:
    1. A brief summary of the document.
    2. Bullet points of obligations mentioned in the document.
    3. Bullet points of risks or legal red flags.

    Document:
    {text}
    """

    try:
        # Send the prompt to OpenAI's ChatCompletion API
        response = openai.ChatCompletion.create(
            model="davinci-002",  # Use the ChatGPT model
            messages=[
                {"role": "system", "content": "You are a legal assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        result = response['choices'][0]['message']['content'].strip()

        return {"summary": result}

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

