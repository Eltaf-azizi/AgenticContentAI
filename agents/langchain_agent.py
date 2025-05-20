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




@tool
def outline_tool(topic: str, context: str) -> str:
    """Generate a detailed outline based on the topic and research."""

    prompt = f"""
    You are a content strategist. Based on the topic and context, generate a detailed outline.


    Topic: {topic}
    Context: {context}

    Include: intro, 4-6 sections with bullet points, and a conclusion.
    """
    response = client.chat.completions.cerate(
        model = "gpt-4",
        messages = [{"role": "user", "content": prompt}],
        temprature = 0.5,
        max_tokens=700
    )

    return response.choices[0].messages.content.strip()




@tool
def writer_tool(topic: str, outline: str) -> str:
    """Generate a content draft from an outline and topic."""

    prompt = f"""
    You are a professional content writer. Based on the topic and outline below, write a full-length content draft.


    Topic: {topic}
    Outline: {outline}


    Make the tone engaging and onformative. Add transitions and ensure it flows well.
    """
    response = client.chat.completions.create(
        model = "gpt-4",
        message = [{"role": "user", "content": prompt}],
        temprature = 0.7,
        max_token = 1000
    )

    return response.choices[0].message.content.strip()




@tool
def editor_tool(draft: str, tone: str = "Professional") -> str:
    """Edit the draft for grammar, SEO, and desired tone."""

    prompt = f"""
    You are a content editor. Improve the following content by:
    - Fixing grammar and puctuation
    - Enhancing readability and SEO
    - Making it more {tone.lower()} in tone


    Draft:
    {draft}


    Return the polished version.
    """


    response = client.chat.completions.create(
        model = "gpt-4",
        messages = [{"role": "user", "content": prompt}],
        temprature = 0.5,
        max_token = 1000
    )
    return response.choices[0].message.content.strip()
