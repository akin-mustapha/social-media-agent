from langchain_core.tools import tool
from src.agent.core import config

@tool
def generate_image_from_prompt(prompt: str) -> str:
    """
    Generates an image based on a descriptive prompt.
    Returns the response from the image generation model, which should include a URL to the generated image.
    Use this to create visuals for social media posts.
    """
    try:
        # Use the singleton LLM client from config and return the string content.
        # This assumes your image gen model returns a URL or useful text.
        response = config.image_gen_llm.invoke(prompt)
        print(f"Image generation model returned: {response.content}")
        return response.content
    except Exception as e:
        return f"Error generating image: {e}"