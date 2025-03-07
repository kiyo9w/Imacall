import elevenlabs
from flask import Flask, request, jsonify, send_file
import requests
import os

app = Flask(__name__)

API_KEY = "sk_8665cf06e56bd84699fbfce8c2e20c8e6f2cf06cf364abe2"
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"
ELEVENLABS_API_URL = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

@app.route("/api/test-voice", methods=["POST"])
def test_voice():
    try:
        data = request.get_json()
        text = data.get("text")

        if not text:
            return jsonify({"error": "Missing 'text' field"}), 400
        headers = {
            "Content-Type": "application/json",
            "xi-api-key": API_KEY
        }
        payload = {
            "text": text,
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }
        response = requests.post(ELEVENLABS_API_URL, json=payload, headers=headers)

        if response.status_code != 200:
            return jsonify({"error": "Failed to generate voice", "details": response.text}), response.status_code
        audio_path = "output.mp3"
        with open(audio_path, "wb") as f:
            f.write(response.content)

        return send_file(audio_path, mimetype="audio/mpeg", as_attachment=True, download_name="output.mp3")

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
