from flask import Flask, render_template, request, jsonify
from emotion_detector import detect_emotion, map_emotion_to_voice
from tts_engine import generate_speech

app = Flask(__name__)

# THIS is the only source of truth for rate/pitch
EMOTION_PARAMS = {
    "joy":      {"rate": "+25%", "pitch": "+8Hz"},
    "surprise": {"rate": "+30%", "pitch": "+10Hz"},
    "anger":    {"rate": "+15%", "pitch": "-5Hz"},
    "fear":     {"rate": "-20%", "pitch": "+3Hz"},
    "sadness":  {"rate": "-25%", "pitch": "-8Hz"},
    "disgust":  {"rate": "-10%", "pitch": "-5Hz"},
    "neutral":  {"rate": "+0%",  "pitch": "+0Hz"},
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"error": "No text provided"}), 400

    emotion_result = detect_emotion(text)
    voice_config   = map_emotion_to_voice(emotion_result)
    audio_filename = generate_speech(text, voice_config)

    emotion = voice_config["emotion"]
    params  = EMOTION_PARAMS.get(emotion, EMOTION_PARAMS["neutral"])

    # This MUST print the correct rate/pitch — check your terminal
    print("=" * 50)
    print(f"EMOTION  : {emotion}")
    print(f"RATE     : {params['rate']}")
    print(f"PITCH    : {params['pitch']}")
    print("=" * 50)

    return jsonify({
        "emotion":      emotion,
        "confidence":   voice_config["confidence"],
        "description":  voice_config["description"],
        "all_emotions": emotion_result["all_emotions"],
        "rate":         params["rate"],
        "pitch":        params["pitch"],
        "audio_url":    f"/static/{audio_filename}"
    })

if __name__ == "__main__":
    # app.run(debug=True, use_reloader=False)
    app.run(host="0.0.0.0", port=port)