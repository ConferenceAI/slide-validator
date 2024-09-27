from app.services.deterministic_checks import run_checks, check_file_size, check_format
from app.models.slide_deck import SlideDeck


def test_run_checks():
    slide_deck = SlideDeck(content=b"test" * 1000,
                           filename="test.pdf",
                           file_format="PDF")
    results = run_checks(slide_deck)
    assert isinstance(results, dict)
    assert "file_size" in results
    assert "slide_count" in results
    assert "format_valid" in results


def test_check_file_size():
    small_deck = SlideDeck(content=b"test",
                           filename="small.pdf",
                           file_format="PDF")
    assert check_file_size(small_deck) == True

    large_deck = SlideDeck(content=b"test" * 10**6,
                           filename="large.pdf",
                           file_format="PDF")
    assert check_file_size(large_deck) == False


def test_check_format():
    valid_deck = SlideDeck(content=b"test",
                           filename="valid.pdf",
                           file_format="PDF")
    assert check_format(valid_deck) == True

    invalid_deck = SlideDeck(content=b"test",
                             filename="invalid.txt",
                             file_format="Unknown")
    assert check_format(invalid_deck) == False
