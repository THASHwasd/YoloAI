# YOLO Assistant v1.0.3 - Powered by Mistral
# Created by ThashWASD
#
# ⚠️ DO NOT DEPLOY ⚠️
# This is a fun local project. Do not incorporate this code into production systems,
# as it hardcodes API keys and is not secure or suitable for public deployment.
#
# ✅ Usage Notes:
# - Follow the MIT License terms.
# - Comply with OpenRouter's Terms and Conditions before use.
# - Intended for **local** experimentation and educational purposes only.
# - 🚧 Go wild, but don’t blame me! 
# - ThashWASD takes no responsibility for what happens when you use or modify this code.

import requests

# TODO: Insert your OpenRouter API key below
API_KEY = '{ENTER API KEY HERE}'

# Model settings
MODEL = "mistralai/mistral-7b-instruct"
HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json',
    'HTTP-Referer': 'http://localhost',
    'X-Title': 'YOLO Assistant'
}

def ask_ai(prompt, name):
    # Send prompt to Mistral AI via OpenRouter API and return the assistant's reply.
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": f"You are a helpful assistant deployed by THASHwasd for educational purposes. Your user is {name}."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post('https://openrouter.ai/api/v1/chat/completions', headers=HEADERS, json=data)
        result = response.json()
        if response.status_code == 200:
            return result["choices"][0]["message"]["content"]
        else:
            return f"Error: {result.get('error', 'Unknown error')}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"

# Entry point
if __name__ == "__main__":
    print("🧠 YOLO Assistant (v1.0.3) - Type 'exit' to quit\n")

    name = input("What's your name? ").strip()
    print(f"👋 Hello, {name}! Let's get started.\n")

    while True:
        user_input = input(f"{name}: ")
        if user_input.lower() in ["exit", "quit"]:
            print(f"YOLO: Goodbye, {name}!")
            break
        elif user_input.lower() == "who made you?":
            print("YOLO: I was developed by ThashWASD using the Mistral AI model.")
        else:
            response = ask_ai(user_input, name)
            print("YOLO:", response)
