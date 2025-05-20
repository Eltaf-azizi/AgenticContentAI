from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda
from agents.langchain_agent import (
    research_tool,
    outline_tool,
    writer_tool,
    editor_tool,
    seo_tool
)



# Define state type
from typing import TypedDict