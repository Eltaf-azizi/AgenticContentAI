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





# Node: Outline
def outline_node(state: AgentState) -> AgentState:
    outline = outline_tool.invoke({
        "topic": state["topic"],
        "context": state["context"]
    })
    return {**state, "outline": outline}



# Node: Writer
def writer_node(state: AgentState) -> AgentState:
    draft = writer_tool.invoke({
        "topic": state["topic"],
        "outline": state["outline"]
    })
    return {**state, "draft": draft}



# Node: Editor (with tone)
def editor_node(state: AgentState) -> AgentState:
    final = editor_tool.invoke({
        "draft": state["draft"],
        "tone": state.get("tone", "Professional")
    })
    return {**state, "final": final}




# Node: SEO
def seo_node(state: AgentState) - > AgentState: