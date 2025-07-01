from langchain_core.tools import tool
from src.agent.image_generators.gemini_generator import GeminiImageGenerator
from src.agent.image_generators.dalle_generator import DalleImageGenerator
from src.agent.core import config
# --- The "Plug and Play" Factory ---

# Create instances of all available generators
available_generators = {
    "gemini": GeminiImageGenerator(),
    "dalle": DalleImageGenerator()
}


def get_image_generator():
    """Returns the currently selected image generator instance."""
    return available_generators.get(config.selected_image_gen_llm)

# --- The Unified LangChain Tool ---

@tool
def generate_image(prompt: str) -> str:
    """
    Use this tool to generate an image based on a descriptive prompt.
    It will create a visual for a social media post and return a URL to the image.
    """
    generator = get_image_generator()
    if not generator:
        return f"Error: The selected image generator '{config.selected_image_gen_llm}' is not available."

    print(f"Using {config.selected_image_gen_llm} to generate image...")
    return generator.generate(prompt)