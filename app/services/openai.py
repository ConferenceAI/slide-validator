import os
import openai
from typing import List

class OpenAIService:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    async def generate_text(self, prompt: str, max_tokens: int = 100) -> str:
        try:
            response = await openai.Completion.acreate(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=max_tokens
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"Error in OpenAI text generation: {str(e)}")
            return ""

    async def analyze_image(self, image_url: str) -> List[str]:
        try:
            response = await openai.Image.acreate(
                prompt="What's in this image?",
                image=image_url,
                max_tokens=50
            )
            return response.choices[0].text.strip().split(", ")
        except Exception as e:
            print(f"Error in OpenAI image analysis: {str(e)}")
            return []
