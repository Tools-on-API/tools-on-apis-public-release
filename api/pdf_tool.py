from quart import Blueprint, request, jsonify
import PyPDF2

pdf_bp = Blueprint("pdf_tool", __name__)

@pdf_bp.route("/extract-pdf-text", methods=["POST"])
async def extract_pdf():
    file = (await request.files).get("file")
    if not file:
        return jsonify({"error": "PDF file required"}), 400

    try:
        reader = PyPDF2.PdfReader(file)
        text = "\n".join([page.extract_text() or "" for page in reader.pages])
        return jsonify({"text": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
