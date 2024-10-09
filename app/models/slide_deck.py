from pydantic import BaseModel, Field
from typing import List, Optional


class SlideDeck(BaseModel):
    url: Optional[str] = None
    content: bytes

    filename: str
    file_format: str
    file_extension: str = Field(
        ..., description="File extension (e.g., 'pdf', 'pptx')")

    file_size: int = Field(..., description="Size of the file in bytes")
    slide_count: Optional[int] = Field(None, description="Number of slides")
    image_count: Optional[int] = Field(None, description="Number of images")
    audio_count: Optional[int] = Field(None,
                                       description="Number of audio files")
    video_count: Optional[int] = Field(None, description="Number of videos")
    bullet_count: Optional[int] = Field(None,
                                        description="Number of bullet points")
    fonts_used: Optional[List[str]] = Field(
        None, description="List of fonts used in the slide deck")

    class Config:
        arbitrary_types_allowed = True  # This allows us to use bytes for content

    def __str__(self):
        return (
            f"SlideDeck(filename={self.filename}, file_format={self.file_format},"
            f"file_extension={self.file_extension}, file_size={self.file_size} bytes, "
            f"slide_count={self.slide_count}, image_count={self.image_count}, "
            f"audio_count={self.audio_count}, video_count={self.video_count}, "
            f"bullet_count={self.bullet_count}, fonts_used={self.fonts_used})")
