from abc import ABC, abstractmethod

class BaseImageGenerator(ABC):
    """
    Abstract base class for all image generation models.
    Defines a standard interface for the agent to interact with.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generates an image based on a descriptive prompt.

        Args:
            prompt (str): The text prompt describing the desired image.

        Returns:
            str: The URL of the generated image.
        """
        pass