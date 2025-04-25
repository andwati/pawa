from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints.summarize import summarize_document

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(summarize_document.router, prefix="/api/v1/summarize", tags=["summarize"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Legal Document Summarizer API"}