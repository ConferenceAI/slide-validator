from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

class ClaudeService:
    def __init__(self, api_key: str):
        self.client = Anthropic(api_key=api_key)

    async def generate_text(self, prompt: str, max_tokens_to_sample: int = 100) -> str:
        try:
            response = await self.client.completions.create(
                prompt=f"{HUMAN_PROMPT} {prompt}{AI_PROMPT}",
                max_tokens_to_sample=max_tokens_to_sample,
                model="claude-2.0"
            )
            return response.completion
        except Exception as e:
            print(f"Error in Claude text generation: {str(e)}")
            return ""
