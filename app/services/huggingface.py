from transformers import pipeline
from typing import List, Dict

class HuggingFaceService:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def sentiment_analysis(self, text: str) -> Dict[str, float]:
        try:
            sentiment_pipeline = pipeline("sentiment-analysis")
            result = sentiment_pipeline(text)[0]
            return {
                "label": result["label"],
                "score": result["score"]
            }
        except Exception as e:
            print(f"Error in HuggingFace sentiment analysis: {str(e)}")
            return {"label": "ERROR", "score": 0.0}

    async def text_generation(self, prompt: str, max_length: int = 50) -> str:
        try:
            generator = pipeline("text-generation", model="gpt2")
            result = generator(prompt, max_length=max_length, num_return_sequences=1)
            return result[0]["generated_text"]
        except Exception as e:
            print(f"Error in HuggingFace text generation: {str(e)}")
            return ""

