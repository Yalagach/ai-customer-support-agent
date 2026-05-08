from flask import Flask, request, jsonify, render_template, send_from_directory
from gtts import gTTS
import os
import requests
from datetime import datetime

#from openai import OpenAI

app = Flask(__name__)

#client = OpenAI()
#openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_response(user_input):

    user_input = user_input.lower()

    if "loan balance" in user_input:
        return """
Welcome to Crescent Finance.
Your current loan balance is $4,250.
"""

    elif "payment due" in user_input:
        return """
Your next payment of $300 is due on May 20th.
Would you like to make a payment online?
"""

    elif "late fee" in user_input:
        return """
I understand you're calling about a late payment.
A late fee may apply after 10 days past due.
Would you like to speak with customer care during business hours?
"""

    elif "customer care" in user_input:
        return """
Our customer care team is currently unavailable.
Business hours are Monday through Friday, 8 AM to 5 PM Eastern Time.
Your callback request has been successfully recorded.
"""

    response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3",
        "prompt": f"""
    You are a customer support agent for Crescent Finance.

    Rules:
    - Respond in 3 to 4 short sentences only.
    - Be clear, polite, and professional.
    - Do not use bullet points.
    - Do not be verbose.

    Customer: {user_input}

    Answer:
    """,
            "stream": False
        }
    )

    data = response.json()
    return data["response"]


def text_to_speech(text):
    tts = gTTS(text)

    os.makedirs("responses", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"responses/response_{timestamp}.mp3"

    tts.save(filename)

    return filename

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    print(f"[{datetime.now()}] Customer asked: {user_input}")
    reply = get_ai_response(user_input)
    audio_file = text_to_speech(reply)

    return jsonify({
        "response": reply,
        "audio": audio_file
    })

@app.route("/responses/<filename>")
def serve_audio(filename):
    return send_from_directory("responses", filename)

if __name__ == "__main__":
    app.run(debug=True, port=5001)