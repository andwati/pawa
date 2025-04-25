from pydantic import BaseModel

class Summary(BaseModel):
    summary: str
    word_count: int
    character_count: int