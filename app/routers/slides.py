import traceback
from fastapi import APIRouter, UploadFile, File, Form

from app.models.slide_deck import SlideDeck
from app.utils import file_handler, deterministic_checks, probabilistic_checks

router = APIRouter(
    prefix="/slides",
    tags=["slides"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.post("/validate")
async def validate_slide_deck(file: UploadFile = File(None),
                              url: str = Form(None)):
    if file is None and url is None:
        return {"error": "Either file or URL must be provided"}
    try:
        print("Processing input...")
        slide_deck = await file_handler.process_input(file, url)

        # Perform deterministic checks
        deterministic_results = deterministic_checks.run_checks(slide_deck)

        # Perform probabilistic checks
        probabilistic_results = await probabilistic_checks.run_checks(slide_deck)

        # Combine results
        all_checks = {**deterministic_results, **probabilistic_results}

        validation_response = {
            "validation": all(all_checks.values()),
            "checks": all_checks,
            "meta": {   
                "file_format": slide_deck.file_format,
                "file_size (KB)": round(slide_deck.file_size / (1024), 2),
                "slide_count": slide_deck.slide_count,
                "image_count": slide_deck.image_count,
                "audio_count": slide_deck.audio_count,
                "video_count": slide_deck.video_count,
            },
        }
        print(validation_response)
        return validation_response
    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}


@router.post("/submit")
async def submit_slide_deck(slide_deck: SlideDeck):
    # Logic to submit a validated slide deck
    # This could include merging into a master deck
    return {"message": "Slide deck submitted successfully"}
