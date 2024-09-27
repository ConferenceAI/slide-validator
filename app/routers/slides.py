from fastapi import APIRouter, UploadFile, File, Form
from app.services import file_handler, deterministic_checks, ai_checks
from app.models.slide_deck import SlideDeck

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
    try:
        slide_deck = await file_handler.process_input(file, url)

        # Perform deterministic checks
        deterministic_results = deterministic_checks.run_checks(slide_deck)

        # Perform AI checks
        ai_results = await ai_checks.run_checks(slide_deck)

        # Combine results
        all_results = {**deterministic_results, **ai_results}

        return {
            "results": all_results,
            "all_passed": all(all_results.values())
        }
    except Exception as e:
        return {"error": str(e)}


@router.post("/submit")
async def submit_slide_deck(slide_deck: SlideDeck):
    # Logic to submit a validated slide deck
    # This could include merging into a master deck
    return {"message": "Slide deck submitted successfully"}
