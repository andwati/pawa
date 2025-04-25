from pydantic import BaseModel
from typing import Optional

class Document(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    file_type: str  # 'pdf' or 'txt'
    uploaded_at: Optional[str] = None  # Timestamp of when the document was uploaded

    class Config:
        orm_mode = True