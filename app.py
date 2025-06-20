import asyncio
import socket
import requests
from concurrent.futures import ThreadPoolExecutor as NamedThreadPoolExecutor
from quart import Quart, jsonify, request, abort
from uvicorn import Config, Server
import os
# === Application Setup ===
app = Quart(__name__)

# === Health Check ===
@app.route("/healthz")
async def health():
    return jsonify({"status": "ok"})

@app.route("/", methods=["GET"])
def greet_json():
    return jsonify({"message": "Hello World!"}), 200

# === Blueprint Imports ===
from api.uuid_tool import uuid_bp
from api.encrypt_tool import encrypt_bp
from api.pdf_tool import pdf_bp
from api.qrcode_tool import qrcode_bp
from api.regex_tool import regex_bp
from api.assistant_tool import assistant_bp

app.register_blueprint(uuid_bp, url_prefix="/api")
app.register_blueprint(encrypt_bp, url_prefix="/api")
app.register_blueprint(pdf_bp, url_prefix="/api")
app.register_blueprint(qrcode_bp, url_prefix="/api")
app.register_blueprint(regex_bp, url_prefix="/api")
app.register_blueprint(assistant_bp, url_prefix="/api")

# === Utility ===
def get_server_host_port():
    import os
    return os.getenv("HOST", "0.0.0.0"), os.getenv("PORT", "10000")

def debug_print(msg):
    print(f"[DEBUG] {msg}")

def custom_print(msg):
    print(msg.replace("{green}", "\033[92m").replace("{red}", "\033[91m").replace("{reset}", "\033[0m"))

# === Custom UVicorn Runner ===
if __name__ == "__main__":
    app.run()
