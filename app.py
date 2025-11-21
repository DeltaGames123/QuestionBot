# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot activo"

@app.route('/health')
def health():
    return "ok"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
