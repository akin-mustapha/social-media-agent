#initializes and provides singleton clients for APIs and LLMs.
import tweepy
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

# --- Twitter/X API Clients ---
# It's good practice to initialize these once and reuse them.
twitter_v2_client = tweepy.Client(
    bearer_token=os.getenv("X_BEARER_TOKEN"),
    consumer_key=os.getenv("X_API_KEY"),
    consumer_secret=os.getenv("X_API_SECRET_KEY"),
    access_token=os.getenv("X_ACCESS_TOKEN"),
    access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET"),
)

auth_v1 = tweepy.OAuth1UserHandler(
    consumer_key=os.getenv("X_API_KEY"),
    consumer_secret=os.getenv("X_API_SECRET_KEY"),
    access_token=os.getenv("X_ACCESS_TOKEN"),
    access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET"),
)
twitter_v1_api = tweepy.API(auth_v1)

# --- LLM Clients ---
# LLM for generating text (the agent's brain)
text_gen_llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.7,google_api_key=os.getenv('GOOGLE_API_KEY'))

# LLM for generating images
gemini_image_gen_llm = ChatGoogleGenerativeAI(model="imagen-4.0-generate-preview-06-06")

print("Configuration loaded: API and LLM clients initialized.")