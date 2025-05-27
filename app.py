from flask import Flask, json, request, jsonify, render_template
from AgentIQ.examples.researcher_agent.researcher_agent import search_web
from fusecore import mistral_response
from oracle_mirror import oracle_response
from guardian_ai import guardian_critique_response
from image_generator import generate_image
from openhermes import openhermes_response
import json
from datetime import datetime
from fusecore import fusecore_response


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

import os
import requests
from flask import request, jsonify

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY") # Set your NVIDIA_API_KEY in environment variables before running

@app.route("/ask-agent", methods=["POST"])
def ask_agent():
    data = request.get_json()
    query = data.get("query", "")

    try:
        result = search_web(query)
        return jsonify({"response": result})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/generate-image", methods=["POST"]) 
def generate_image_route():
    data = request.get_json()
    prompt = data.get("prompt")
    style = data.get("style")  # You can use this later if you want to customize

    try:
        image_path = generate_image(prompt)
        url = "/" + image_path.replace("\\", "/")  # Convert path to URL format
        return jsonify({"url": url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("prompt")
    model = data.get("model")

    if not prompt or not model:
        return jsonify({"error": "Missing prompt or model"}), 400

    try:
        if model == "mistral":
            result = mistral_response(prompt)
        elif model == "oracle":
            result = oracle_response(prompt)
        elif model == "openhermes":
            result = openhermes_response(prompt)
        elif model == "fusecore":
            mistral_out = mistral_response(prompt)
            openhermes_out = openhermes_response(prompt)

            try:
                guardian_out = guardian_critique_response(prompt, mistral_out, openhermes_out)
            except Exception as e:
                guardian_out = f"⚠️ Guardian critique failed: {str(e)}"

            result = fusecore_response(prompt, mistral_out, openhermes_out, guardian_out)



        else:
            result = "Unknown model selected."

        log = {
            "timestamp": datetime.utcnow().isoformat(),
            "model": model,
            "prompt": prompt,
            "response": result
        }

        with open("chat_history.json", "a", encoding="utf-8") as f:
            f.write(json.dumps(log) + "\n")

        return jsonify({
            "response": result
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/chat-history", methods=["GET"])
def chat_history():
    try:
        with open("chat_history.json", "r", encoding="utf-8") as f:
            lines = f.readlines()
            history = [json.loads(line) for line in lines]
        return jsonify({"history": history})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/clear-history", methods=["POST"])
def clear_history():
    try:
        with open("chat_history.json", "w", encoding="utf-8") as f:
            f.write("")  # Empty the file
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, threaded=True)
