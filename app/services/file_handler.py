import os
import aiohttp
from fastapi import UploadFile
from app.models.slide_deck import SlideDeck


async def process_input(file: UploadFile = None, url: str = None) -> SlideDeck:
    if file:
        return await process_file(file)
    elif url:
        return await process_url(url)
    else:
        raise ValueError("Either file or URL must be provided")


async def process_file(file: UploadFile) -> SlideDeck:
    content = await file.read()
    filename = file.filename
    file_format = determine_format(filename)
    return SlideDeck(content=content,
                     filename=filename,
                     file_format=file_format)


async def process_url(url: str) -> SlideDeck:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.read()
            filename = url.split("/")[-1]
            file_format = determine_format(filename)
            return SlideDeck(content=content,
                             filename=filename,
                             file_format=file_format,
                             url=url)


def determine_format(filename: str) -> str:
    ext = os.path.splitext(filename)[1].lower()
    format_map = {
        '.pdf': 'PDF',
        '.pptx': 'PowerPoint',
        '.key': 'Keynote',
        '.fig': 'Figma',
        # Add more mappings as needed
    }
    return format_map.get(ext, 'Unknown')
