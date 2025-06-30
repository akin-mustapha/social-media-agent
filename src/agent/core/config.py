#initializes and provides singleton clients for APIs and LLMs.
import tweepy
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

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
text_gen_llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)

# LLM for generating images
image_gen_llm = ChatGoogleGenerativeAI(model="gemini-pro-vision")

print("Configuration loaded: API and LLM clients initialized.")