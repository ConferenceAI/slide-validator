import os
import magic
import aiohttp
from io import BytesIO
from urllib.parse import urlparse

from fastapi import UploadFile

from app.models.slide_deck import SlideDeck
from app.utils.file_analyzer import analyze_file


async def process_input(file: UploadFile = None, url: str = None) -> SlideDeck:
    if file:
        print("Processing file...")
        return await process_file(file)
    elif url:
        print("Processing URL...")
        return await process_url(url)
    else:
        raise ValueError("Either file or URL must be provided")


async def process_file(file: UploadFile) -> SlideDeck:
    content = await file.read()
    filename = file.filename

    mime = magic.Magic(mime=True)
    file_format = mime.from_buffer(content)
    if not file_format:
        print("Warning: file_format is empty.")
        file_format = "unknown"

    file_extension = os.path.splitext(filename)[1][1:].lower()

    file_size = len(content)

    analysis = analyze_file(content, filename, file_format)

    slide_deck = SlideDeck(content=content,
         filename=filename,
         file_format=file_format,
         file_extension=file_extension,
         file_size=file_size,
         slide_count=analysis['slide_count'],
         image_count=analysis['image_count'],
         audio_count=analysis['audio_count'],
         video_count=analysis['video_count'],
         bullet_count=analysis['bullet_count'],
         fonts_used=analysis['fonts_used'])

    return slide_deck


async def process_url(url: str) -> SlideDeck:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.read()
            filename = url.split("/")[-2]
            return await process_file(
                UploadFile(filename=filename, file=BytesIO(content)))
