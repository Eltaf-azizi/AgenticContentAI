import os
from flask import Flask, render_template, request, url_for
from agents.langgraph_pipeline import graph
from agents.langchain_pipeline import chain
from agents.image_agent import generate_image
from utils.exporter import save_as_markdown, save_as_pdf



app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        topic = request.form.get("topic")
        content_type = request.form.get("content_type")
        tone = request.form.get("tone")
        pipeline = request.form.get("pipeline") # pipeline toggle


        combined_topic = f"{topic} ({content_type})"



        # Toggle between LangGraph and Classic Chain
        if pipeline == "chain":
            result = chain.invoke({
                "topic": combined_topic,
                "tone": tone
            })
        else:
            result = graph.invoke({
                "topic": combined_topic,
                "tone": tone
            })