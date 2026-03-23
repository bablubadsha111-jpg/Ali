from flask import Flask, request, send_file, jsonify
from gtts import gTTS
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # ✅ CORS enable

# ✅ Home route
@app.route("/")
def home():
    return "Server Running ✅"

# ✅ TTS route
@app.route("/tts", methods=["POST"])
def generate_tts():
    try:
        data = request.get_json()

        if not data or "text" not in data:
            return jsonify({"error": "No text provided"}), 400

        text = data["text"]
        print("📥 Text received:", text)

        filename = "output.mp3"

        # ✅ पुरानी file delete
        if os.path.exists(filename):
            os.remove(filename)

        # ✅ TTS generate
        tts = gTTS(text=text, lang="en")
        tts.save(filename)

        print("✅ Audio generated")

        return send_file(filename, mimetype="audio/mpeg")

    except Exception as e:
        print("❌ ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


# ✅ Run local (Render ignore करेगा)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
