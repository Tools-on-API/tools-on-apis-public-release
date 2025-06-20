from quart import Blueprint, request, jsonify
import re

regex_bp = Blueprint("regex_tool", __name__)

@regex_bp.route("/test-regex", methods=["POST"])
async def test_regex():
    data = await request.get_json()
    pattern = data.get("pattern")
    text = data.get("text")

    if not pattern or text is None:
        return jsonify({"error": "pattern and text required"}), 400

    try:
        matches = [m.group(0) for m in re.finditer(pattern, text)]
        return jsonify({"matches": matches})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
