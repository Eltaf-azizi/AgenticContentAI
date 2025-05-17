import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_outline(topic: str, content: str) -> str:
    prompt = f"""
    You are a content strategist. Based on the following topic and context, generate a detailed outline for a blog or script.


    topic: {topic}
    """