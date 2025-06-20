from quart import Blueprint, request, jsonify
from openai import OpenAI
import os, asyncio

assistant_bp = Blueprint("assistant_tool", __name__)

# import pathlib

# AIML_API_KEY = os.getenv("AIML_API_KEY")
# if AIML_API_KEY is None:
#     env_file = pathlib.Path("app.py").parent / ".env"
#     if env_file.exists():
#         with open(env_file) as f:
#             for line in f.read().splitlines():
#                 if line.startswith("AIML_API_KEY"):
#                     AIML_API_KEY = line.split("=")[1].strip()
#                     break
#     if AIML_API_KEY is None:
#         raise RuntimeError("AIML_API_KEY not found in environment or .env file. Searched for path: " + str(env_file))

# client = OpenAI(
#     base_url="https://api.aimlapi.com/v1",
#     api_key=AIML_API_KEY,
# )

@assistant_bp.route("/chat", methods=["POST"])
async def chat():
    return jsonify({"message": "This route is still in development"}), 400


# async def chat():
#     data = await request.get_json()
#     prompt = data.get("prompt", "")

#     if not prompt:
#         return jsonify({"error": "Prompt required"}), 400

#     try:
#         response = await asyncio.to_thread(lambda: client.chat.completions.create(
#             model="google/gemma-3n-e4b-it",
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.7,
#             top_p=0.7,
#             stream=False
#         ))
#         message = response.choices[0].message.content
#         return jsonify({"response": message})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
