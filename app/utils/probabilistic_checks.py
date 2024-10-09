import os
from app.services.openai import OpenAIService
from app.models.slide_deck import SlideDeck

openai_service = OpenAIService(os.environ['OPENAI_API_KEY'])

async def run_checks(slide_deck: SlideDeck) -> dict:
    results = {
        "content_appropriate": await check_content_appropriateness(slide_deck),
        "style_consistent": await check_style_consistency(slide_deck),
        "grammar_correct": await check_grammar(slide_deck),
    }
    return results

async def check_content_appropriateness(slide_deck: SlideDeck) -> bool:
    # Implement content appropriateness check using AI

    openai_text = await openai_service.generate_text("Write a short story about a robot.")
    print("OpenAI generated text:", openai_text)
    
    return True


async def check_style_consistency(slide_deck: SlideDeck) -> bool:
    return True


async def check_grammar(slide_deck: SlideDeck) -> bool:
    return True