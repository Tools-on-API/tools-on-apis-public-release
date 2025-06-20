from quart import Blueprint, request, send_file, jsonify
import qrcode, io
from qrcode.constants import ERROR_CORRECT_M
from qrcode.exceptions import DataOverflowError

qrcode_bp = Blueprint("qrcode_tool", __name__)

@qrcode_bp.route("/generate-qrcode", methods=["POST"])
async def generate_qr():
    data = await request.get_json()
    text = data.get("text")

    if not text:
        return jsonify({"error": "text required"}), 400

    if len(text) > 3000:
        return jsonify({"error": "Text too long. Max allowed is 3000 characters."}), 400

    try:
        qr = qrcode.QRCode(
            version=None,  # Let qrcode determine the smallest version needed
            error_correction=ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image()

        buf = io.BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)
        return await send_file(buf, mimetype="image/png")

    except DataOverflowError:
        return jsonify({"error": "Data too large to encode in QR code."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
