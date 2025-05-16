import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def research_topic(topic: str) -> str:
    prompt = f"""
    You are a research assistant. Provide a detailed overview of the topic: "{topic}".
    Include current trends,
"""