from quart import Blueprint, request, jsonify
import uuid

uuid_bp = Blueprint("uuid_tool", __name__)

@uuid_bp.route("/generate-uuid", methods=["GET"])
async def generate_uuid():
    version = request.args.get("version", "4")
    name = request.args.get("name")
    namespace = request.args.get("namespace")

    try:
        if version == "1":
            generated = str(uuid.uuid1())
        elif version == "3":
            if not name or not namespace:
                return jsonify({"error": "name and namespace required"}), 400
            generated = str(uuid.uuid3(uuid.UUID(namespace), name))
        elif version == "4":
            generated = str(uuid.uuid4())
        elif version == "5":
            if not name or not namespace:
                return jsonify({"error": "name and namespace required"}), 400
            generated = str(uuid.uuid5(uuid.UUID(namespace), name))
        else:
            return jsonify({"error": "Invalid version"}), 400

        return jsonify({"uuid": generated, "version": version})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
