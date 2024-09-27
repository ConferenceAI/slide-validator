from app.models.slide_deck import SlideDeck


def run_checks(slide_deck: SlideDeck) -> dict:
    # Implement deterministic checks here
    # For example:
    results = {
        "file_size": check_file_size(slide_deck),
        "slide_count": check_slide_count(slide_deck),
        "format_valid": check_format(slide_deck),
    }
    return results


def check_file_size(slide_deck: SlideDeck) -> bool:
    # Implement file size check
    return len(slide_deck.content) < 10 * 1024 * 1024  # 10 MB limit


def check_slide_count(slide_deck: SlideDeck) -> bool:
    # Implement slide count check
    # This is a placeholder and would need actual implementation
    return True


def check_format(slide_deck: SlideDeck) -> bool:
    valid_formats = ['PDF', 'PowerPoint', 'Keynote', 'Figma']
    return slide_deck.file_format in valid_formats
