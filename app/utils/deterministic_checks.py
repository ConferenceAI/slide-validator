import io
import zipfile
import PyPDF2

from app.models.slide_deck import SlideDeck

# TODO: Make these variables configurable via admin interface.
VALID_FILE_FORMATS = [
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    "application/vnd.ms-powerpoint",
    "application/vnd.oasis.opendocument.presentation",
    "application/vnd.apple.keynote",
    "image/svg+xml",
]
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100 MB
MAX_SLIDES = 50
BANNED_FONT_TYPES = [
]

def run_checks(slide_deck: SlideDeck) -> dict:
    results = {
        "valid_file_format": check_file_format(slide_deck),
        "valid_file_size": check_file_size(slide_deck),
        "valid_slide_count": check_slide_count(slide_deck),
        "valid_fonts_used": check_fonts_used(slide_deck),
    }
    return results

def check_file_format(slide_deck: SlideDeck) -> bool:
    return slide_deck.file_format in VALID_FILE_FORMATS

def check_file_size(slide_deck: SlideDeck) -> bool:
    return slide_deck.file_size <= MAX_FILE_SIZE

def check_slide_count(slide_deck: SlideDeck) -> bool:
    return slide_deck.slide_count <= MAX_SLIDES

def check_fonts_used(slide_deck: SlideDeck) -> bool:
    return all(font not in BANNED_FONT_TYPES for font in slide_deck.fonts_used)