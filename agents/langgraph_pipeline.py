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



class AgentState(TypedDict):
    topic: str
    tone: str
    context: str
    outline: str
    draft: str
    final: str
    keywords: str




# Node: Research
def research_node(state: AgentState) -> AgentState:
    context = research_tool.invoke(state["topic"])
    return {**state, "context": context}