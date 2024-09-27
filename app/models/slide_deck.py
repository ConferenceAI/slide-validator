from pydantic import BaseModel
from typing import Optional


class SlideDeck(BaseModel):
    content: bytes
    filename: str
    file_format: str
    url: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True  # This allows us to use bytes for content
