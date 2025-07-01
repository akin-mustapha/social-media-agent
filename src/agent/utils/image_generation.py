from langchain_core.tools import tool
from src.agent.image_generators.gemini_generator import GeminiImageGenerator
from src.agent.image_generators.dalle_generator import DalleImageGenerator

# --- The "Plug and Play" Factory ---

# Create instances of all available generators
available_generators = {
    "gemini": GeminiImageGenerator(),
    "dalle": DalleImageGenerator()
}

# This is our switch. We can set this in a config file or env var later.
# For now, we'll hard-code it to show the concept.
SELECTED_GENERATOR = "dalle" # <-- CHANGE THIS TO "gemini" TO SWITCH!

def get_image_generator():
    """Returns the currently selected image generator instance."""
    return available_generators.get(SELECTED_GENERATOR)

# --- The Unified LangChain Tool ---

@tool
def generate_image(prompt: str) -> str:
    """
    Use this tool to generate an image based on a descriptive prompt.
    It will create a visual for a social media post and return a URL to the image.
    """
    generator = get_image_generator()
    if not generator:
        return f"Error: The selected image generator '{SELECTED_GENERATOR}' is not available."

    print(f"Using {SELECTED_GENERATOR} to generate image...")
    return generator.generate(prompt)