from flask import Flask, request, jsonify, send_from_directory
import requests, os

app = Flask(__name__)
API_KEY = os.environ.get("DEEPSEEK_API_KEY")
history = [
    {
        "role": "system",
        "content": (
            "You are a CS and coding assistant. Rules:\n"
            "- Only answer CS topics: coding, algorithms, data structures, OS, networking, fundamentals.\n"
            "- Refuse anything unrelated politely in one line.\n"
            "- Always write code in C++ unless the user explicitly asks for another language.\n"
            "- Be concise. No fluff, no long explanations unless asked.\n"
            "- Minimize token usage: short answers, no repetition, no filler words."
        )
    }
]

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json.get("message")
    history.append({"role": "user", "content": msg})
    res = requests.post(
        "https://api.deepseek.com/chat/completions",
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
        json={"model": "deepseek-v4-pro", "messages": history, "max_tokens": 600}
    )
    reply = res.json()["choices"][0]["message"]["content"]
    history.append({"role": "assistant", "content": reply})
    return jsonify({"reply": reply})
@app.route('/')
def home():
    return '<body style="margin:0;background:#fff;display:flex;justify-content:center;align-items:center;height:100vh"><img src="/meme.png" style="max-width:600px;width:100%;border-radius:12px"></body>'

@app.route('/meme.png')
def meme():
    return send_from_directory('.', 'meme.png')
@app.route("/ping")
def ping():
    return "pong", 200

@app.route("/mad.ps1")
def script():
    with open("mad.ps1", "r") as f:
        return f.read(), 200, {"Content-Type": "text/plain"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
