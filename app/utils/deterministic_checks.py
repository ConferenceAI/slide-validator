import io
import zipfile
import PyPDF2

from app.models.slide_deck import SlideDeck

# TODO: Make these variables configurable via admin interface.
MAX_FILE_SIZE = 100 * 1024 * 1024  # 50 MB
MAX_SLIDES = 50
VALID_FORMATS = [
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    "application/vnd.ms-powerpoint",
    "application/vnd.oasis.opendocument.presentation",
    "application/vnd.apple.keynote",
    "image/svg+xml",
]

def run_checks(slide_deck: SlideDeck) -> dict:
    results = {
        "file_size": check_file_size(slide_deck),
        "file_format": check_format(slide_deck),
    }

    # Add format-specific checks
    if slide_deck.file_format == "application/pdf":
        results.update(check_pdf(slide_deck))
    elif slide_deck.file_format in [
            "application/vnd.openxmlformats-officedocument.presentationml.presentation",
            "application/vnd.ms-powerpoint"
    ]:
        results.update(check_powerpoint(slide_deck))
    elif slide_deck.file_format == "application/vnd.oasis.opendocument.presentation":
        results.update(check_odp(slide_deck))

    return results


def check_file_size(slide_deck: SlideDeck) -> bool:
    return len(slide_deck.content) <= MAX_FILE_SIZE


def check_format(slide_deck: SlideDeck) -> bool:
    return slide_deck.file_format in VALID_FORMATS


def check_pdf(slide_deck: SlideDeck) -> dict:
    try:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(slide_deck.content))
        num_pages = len(pdf_reader.pages)
        return {
            "pdf_readable":
            True,
            "slide_count":
            num_pages <= MAX_SLIDES,  # Assuming max 50 slides
            "has_text":
            any(page.extract_text().strip() for page in pdf_reader.pages)
        }
    except:
        return {"pdf_readable": False, "slide_count": False, "has_text": False}


def check_powerpoint(slide_deck: SlideDeck) -> dict:
    try:
        with zipfile.ZipFile(io.BytesIO(slide_deck.content)) as zf:
            slide_files = [
                f for f in zf.namelist() if f.startswith('ppt/slides/slide')
            ]
            return {
                "pptx_valid":
                True,
                "slide_count":
                len(slide_files) <= MAX_SLIDES,  # Assuming max 50 slides
                "has_images":
                any(f.startswith('ppt/media/') for f in zf.namelist())
            }
    except:
        return {"pptx_valid": False, "slide_count": False, "has_images": False}


def check_odp(slide_deck: SlideDeck) -> dict:
    try:
        with zipfile.ZipFile(io.BytesIO(slide_deck.content)) as zf:
            content_xml = zf.read('content.xml').decode('utf-8')
            slide_count = content_xml.count('<draw:page')
            return {
                "odp_valid": True,
                "slide_count": slide_count <= MAX_SLIDES,  # Assuming max 50 slides
                "has_images": '<draw:image' in content_xml
            }
    except:
        return {"odp_valid": False, "slide_count": False, "has_images": False}


# You might want to add more format-specific check functions here
