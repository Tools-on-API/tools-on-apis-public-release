from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

@app.route('/api/index', methods=['GET'])
def index():
    return jsonify({'message': 'Fallback Route. Route you want is /generate-uuid'}), 400


@app.route('/generate-uuid', methods=['GET'])
def generate_uuid():
    version = request.args.get('version', '4')
    name = request.args.get('name')
    namespace = request.args.get('namespace')

    try:
        if version == '1':
            generated = str(uuid.uuid1())
        elif version == '3':
            if not name or not namespace:
                return jsonify({'error': 'name and namespace required for UUID v3'}), 400
            generated = str(uuid.uuid3(uuid.UUID(namespace), name))
        elif version == '4':
            generated = str(uuid.uuid4())
        elif version == '5':
            if not name or not namespace:
                return jsonify({'error': 'name and namespace required for UUID v5'}), 400
            generated = str(uuid.uuid5(uuid.UUID(namespace), name))
        else:
            return jsonify({'error': 'Invalid version. Use 1, 3, 4, or 5.'}), 400

        return jsonify({'uuid': generated, 'version': version}), 200

    except Exception as e:
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
