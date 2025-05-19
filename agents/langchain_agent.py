# agents/langchain_agent.py


import os
from dotenv import load_dotenv
from langchain.tools import tool
from openai import OpenAI



load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



@tool
def research_tool(topic: str) -> str:
    """Research a topic and return detailed background information."""
    
    prompt = f"""
    You are a research assistant. Provide a detailed overview of the topic: "{topic}".
    Include current trends, background, and important points to include a blog or content.
    """

    response = client.chat.completions.create(
        model = "gpt-4",
        message = [{"role": "user", "content": prompt}],
        temprature = 0.7,
        max_tokens = 700
    )

    return response.choices[0].message.content.strip()