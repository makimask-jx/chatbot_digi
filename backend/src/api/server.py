from flask import Flask, request, jsonify, render_template
from ia import ai_engine

template_dir = Path(__file__).resolve().parent / "../../../frontend"
app = Flask(__name__, template_folder=str(template_dir))


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "input" not in data:
        return jsonify({"status": "error", "message": "Missing input field"}), 400

    try:
        raw_text = data["input"]
        ai_response = ai_engine.process_input(raw_text)

        return jsonify({"status": "success", "data": ai_response})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
