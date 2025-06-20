from quart import Blueprint, request, jsonify
import base64, hashlib
from Crypto.Cipher import AES

encrypt_bp = Blueprint("encrypt_tool", __name__)

def pad(text):
    return text + (16 - len(text) % 16) * chr(16 - len(text) % 16)

def unpad(text):
    return text[:-ord(text[-1])]

@encrypt_bp.route("/encrypt", methods=["POST"])
async def encrypt():
    data = await request.get_json()
    text = data.get("text")
    key = data.get("key")

    if not text or not key:
        return jsonify({"error": "text and key required"}), 400

    try:
        key_hash = hashlib.sha256(key.encode()).digest()
        cipher = AES.new(key_hash, AES.MODE_ECB)
        encrypted = cipher.encrypt(pad(text).encode())
        encoded = base64.b64encode(encrypted).decode()
        return jsonify({"cipher": encoded})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@encrypt_bp.route("/decrypt", methods=["POST"])
async def decrypt():
    data = await request.get_json()
    cipher_text = data.get("cipher")
    key = data.get("key")

    if not cipher_text or not key:
        return jsonify({"error": "cipher and key required"}), 400

    try:
        key_hash = hashlib.sha256(key.encode()).digest()
        cipher = AES.new(key_hash, AES.MODE_ECB)
        decrypted = cipher.decrypt(base64.b64decode(cipher_text))
        plain = unpad(decrypted.decode())
        return jsonify({"text": plain})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
