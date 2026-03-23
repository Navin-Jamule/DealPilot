from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)
DEFAULT_MODEL_NAME = "gpt-5-mini"

SYSTEM_PROMPT = """Create a concise description of a product. Respond only in this format. Do not include part numbers.
Title: Rewritten short precise title
Category: eg Electronics
Brand: Brand name
Description: 1 sentence description
Details: 1 sentence on features"""


class Preprocessor:
    def __init__(self, model_name=DEFAULT_MODEL_NAME):
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.model_name = model_name
        self.client = OpenAI()

    def messages_for(self, text: str) -> list[dict]:
        return [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ]

    def preprocess(self, text: str) -> str:
        messages = self.messages_for(text)

        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
            )

            if hasattr(response, "usage") and response.usage:
                self.total_input_tokens += getattr(response.usage, "prompt_tokens", 0)
                self.total_output_tokens += getattr(response.usage, "completion_tokens", 0)

            return response.choices[0].message.content

        except Exception as e:
            print(f"Preprocessor Error: {e}")
            return text  