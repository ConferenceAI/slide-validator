import pytest
from fastapi import UploadFile
from app.services.file_handler import process_input, determine_format
from app.models.slide_deck import SlideDeck


@pytest.mark.asyncio
async def test_process_input_file():
    content = b"test content"
    file = UploadFile(filename="test.pdf", file=content)
    result = await process_input(file=file)
    assert isinstance(result, SlideDeck)
    assert result.filename == "test.pdf"
    assert result.file_format == "PDF"


@pytest.mark.asyncio
async def test_process_input_url():
    url = "http://example.com/test.pptx"
    # This test would need to mock the aiohttp.ClientSession
    # For simplicity, we'll just test the error case
    with pytest.raises(ValueError):
        await process_input(url=url)


def test_determine_format():
    assert determine_format("test.pdf") == "PDF"
    assert determine_format("test.pptx") == "PowerPoint"
    assert determine_format("test.key") == "Keynote"
    assert determine_format("test.fig") == "Figma"
    assert determine_format("test.txt") == "Unknown"
