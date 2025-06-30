from abc import ABC, abstractmethod

class SocialMediaAdapter(ABC):
    """
    Abstract base class for all social media platform adapters.
    Ensures that every adapter has a consistent interface.
    """
    @abstractmethod
    def post(self, content: dict) -> str:
        """
        Posts content to the social media platform.

        Args:
            content (dict): A dictionary containing post data,
                            e.g., {"text": "...", "image_path": "..."}.

        Returns:
            str: A message indicating success or failure.
        """
        pass