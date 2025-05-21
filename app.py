import os
from flask import Flask, render_template, request, url_for
from agents.langgraph_pipeline import graph
from agents.langchain_pipeline import chain
from agents.image_agent import generate_image
from utils.exporter import save_as_markdown, save_as_pdf



app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])