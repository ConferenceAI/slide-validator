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
        all_results = {**deterministic_results, **probabilistic_results}

        validation_response = {
            "results": all_results,
            "all_passed": all(all_results.values()),
            "slide_deck": str(slide_deck)
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
