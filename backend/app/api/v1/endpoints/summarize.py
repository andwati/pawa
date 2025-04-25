from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import Any
from app.services.gemini_api import get_summary

router = APIRouter()

class SummaryResponse(BaseModel):
    summary: str

@router.post("/summarize", response_model=SummaryResponse)
async def summarize_document(file: UploadFile = File(...)) -> SummaryResponse:
    if file.content_type not in ["application/pdf", "text/plain"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF and TXT files are allowed.")
    
    content = await file.read()
    
    summary = await get_summary(content)
    
    return SummaryResponse(summary=summary)