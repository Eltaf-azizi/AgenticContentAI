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
research_chain = RunnableLambda(lambda x: {
    "topic": x["topic"],
    "context": research_tool.invoke(x["topic"])
})



# Step 2: Outline
outline_chain = RunnableLambda(lambda x: {
    "topic": x["topic"],
    "outline": outline_tool.invoke({
        "topic": x["topic"],
        "context": x["context"]
    })
})




# Step 3: Write Draft
write_chain = RunnableLambda(lambda x: {
    
})