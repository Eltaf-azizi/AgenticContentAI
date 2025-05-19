# agents/langchain_agent.py


import os
from dotenv import load_dotenv
from langchain.tools import tool
from openai import OpenAI



load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



@tool
def research_tool(topic: str) -> str: