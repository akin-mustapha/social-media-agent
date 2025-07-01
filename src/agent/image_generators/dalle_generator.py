from openai import OpenAI
from .base_generator import BaseImageGenerator
from src.agent.core import config # We'll need to update config

class DalleImageGenerator(BaseImageGenerator):
    """Image generator using OpenAI's DALL-E model."""

    def __init__(self):
        # We will initialize the OpenAI client here, pulling the key from config
        self.client = OpenAI(api_key=config.openai_api_key)
        print("DalleImageGenerator initialized.")

    def generate(self, prompt: str) -> str:
        """Generates an image using DALL-E 3 and returns its URL."""
        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                n=1,
                size="1024x1024",
                quality="standard",
                response_format="url"
            )
            image_url = response.data[0].url
            return image_url
        except Exception as e:
            return f"Error generating image with DALL-E: {e}"