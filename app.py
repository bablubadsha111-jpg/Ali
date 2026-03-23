from flask import Flask, request, send_file
from gtts import gTTS

app = Flask(__name__)

@app.route("/tts", methods=["POST"])
def tts():
    text = request.json.get("text")
    
    tts = gTTS(text)
    tts.save("output.mp3")

    return send_file("output.mp3", mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
