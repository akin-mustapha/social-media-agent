import json
import requests
from io import BytesIO
from langchain_core.tools import tool

# Import the base adapter and the config clients
from .base_adapter import SocialMediaAdapter
from agent.core import config

class XAdapter(SocialMediaAdapter):
    """Adapter for posting content to X (formerly Twitter)."""

    def __init__(self):
        # Use the singleton clients initialized in config.py
        self.client_v2 = config.twitter_v2_client
        self.api_v1 = config.twitter_v1_api
        print("XAdapter initialized.")

    def post(self, content: dict) -> str:
        """
        Posts a tweet to X, optionally with an image.

        Args:
            content (dict): A dictionary with "text" and optional "image_url".
        """
        text = content.get("text")
        image_url = content.get("image_url")

        if not text:
            return "Error: Tweet text is required."

        media_id = None
        if image_url:
            try:
                response = requests.get(image_url)
                response.raise_for_status()
                image_bytes = BytesIO(response.content)

                # Use the class instance of the v1 API client
                upload_result = self.api_v1.media_upload(filename="image.png", file=image_bytes)
                media_id = upload_result.media_id_string
                print(f"Image uploaded to X with media_id: {media_id}")
            except Exception as e:
                return f"Error uploading image to X: {e}. Please ensure the image_url is valid."

        try:
            if media_id:
                # Use the class instance of the v2 client
                self.client_v2.create_tweet(text=text, media_ids=[media_id])
            else:
                self.client_v2.create_tweet(text=text)
            return "Tweet posted successfully to X!"
        except Exception as e:
            return f"Failed to post tweet to X: {e}"

# --- We also convert the posting logic into a LangChain tool ---
# This allows the agent to call it directly.

# Instantiate the adapter once to be used by the tool
_x_adapter_instance = XAdapter()

@tool
def post_to_x(post_data: str) -> str:
    """
    Use this tool to post content to the social media platform X (formerly Twitter).
    The input must be a JSON string with a "text" key and an optional "image_url" key.
    Example: '{"text": "Hello from my AI agent!", "image_url": "http://image.url/img.png"}'
    """
    try:
        content = json.loads(post_data)
        return _x_adapter_instance.post(content)
    except json.JSONDecodeError:
        return "Error: Input must be a valid JSON string."
    except Exception as e:
        return f"An unexpected error occurred: {e}"