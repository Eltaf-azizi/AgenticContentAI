# agents/langchain_pipeline.py



from agents.langchain_agent import (
    research_tool,
    outline_tool,
    writer_tool,
    editor_tool,
    seo_tool
)
from langchain_core.runnables import RunnableLambda


# Step 1: Research