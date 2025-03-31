from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import json
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Path for storing chat history
HISTORY_FILE = "data/chat_history.json"

# Ensure the history file exists
if not os.path.exists(HISTORY_FILE):
    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
    with open(HISTORY_FILE, "w") as f:
        json.dump([], f)

# Load OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("API key is missing! Set OPENROUTER_API_KEY in .env")

# Request model
class ChatRequest(BaseModel):
    user_input: str

# Load chat history
def load_chat_history():
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)

# Save chat history
def save_chat_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

# Generate response using OpenRouter API (Llama 3.3 70B Instruct)
def generate_response(user_input):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        # "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional
        # "X-Title": "<YOUR_SITE_NAME>",  # Optional
    }
    data = {
        "model": "meta-llama/llama-3.3-70b-instruct:free",
        "messages": [{"role": "user", "content": user_input}],
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"Error: API returned {response.status_code}."
    except requests.exceptions.RequestException:
        return "Error: Unable to connect to OpenRouter API."

# Chat API endpoint
@app.post("/chat/")
def chat(request: ChatRequest):
    chat_history = load_chat_history()
    response = generate_response(request.user_input)

    message_entry = {
        "timestamp": datetime.now().isoformat(),
        "user": request.user_input,
        "bot": response
    }

    chat_history.append(message_entry)
    save_chat_history(chat_history)

    return {"response": response, "timestamp": message_entry["timestamp"]}

# Endpoint to clear chat history
@app.delete("/clear_history/")
def clear_history():
    save_chat_history([])
    return {"message": "Chat history cleared"}
