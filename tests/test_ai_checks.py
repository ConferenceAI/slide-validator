import pytest
from app.services.ai_checks import run_checks
from app.models.slide_deck import SlideDeck


@pytest.mark.asyncio
async def test_run_ai_checks():
    slide_deck = SlideDeck(content=b"test",
                           filename="test.pdf",
                           file_format="PDF")
    results = await run_checks(slide_deck)
    assert isinstance(results, dict)
    assert "content_appropriate" in results
    assert "style_consistent" in results
    assert "grammar_correct" in results
