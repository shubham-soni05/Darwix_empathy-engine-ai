from transformers import pipeline

print("[EmotionDetector] Loading model...")
_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None,
    device=-1
)
print("[EmotionDetector] Model ready ✓")

def detect_emotion(text: str) -> dict:
    try:
        raw   = _classifier(text)
        items = raw[0] if isinstance(raw[0], list) else raw
        normalized = sorted(
            [{"label": i["label"].lower(), "score": round(i["score"], 4)} for i in items],
            key=lambda x: x["score"], reverse=True
        )
        top = normalized[0]
        print(f"[EmotionDetector] '{text[:50]}' → {top['label']} ({top['score']:.2f})")
        return {
            "top_emotion":  top["label"],
            "confidence":   top["score"],
            "all_emotions": {e["label"]: e["score"] for e in normalized}
        }
    except Exception as e:
        print(f"[EmotionDetector] Error: {e}")
        return {"top_emotion": "neutral", "confidence": 1.0, "all_emotions": {"neutral": 1.0}}

def map_emotion_to_voice(emotion_result: dict) -> dict:
    emotion    = emotion_result["top_emotion"]
    confidence = emotion_result["confidence"]
    configs = {
        "joy":      {"description": f"Joy ({confidence:.0%}) — upbeat, faster, higher pitch"},
        "surprise": {"description": f"Surprise ({confidence:.0%}) — quick, raised pitch"},
        "anger":    {"description": f"Anger ({confidence:.0%}) — firm, clipped, lower pitch"},
        "fear":     {"description": f"Fear ({confidence:.0%}) — slow, tense"},
        "sadness":  {"description": f"Sadness ({confidence:.0%}) — slow, subdued, lower pitch"},
        "disgust":  {"description": f"Disgust ({confidence:.0%}) — flat, deliberate"},
        "neutral":  {"description": "Neutral — standard, clear delivery"},
    }
    cfg = configs.get(emotion, configs["neutral"]).copy()
    cfg["emotion"]    = emotion
    cfg["confidence"] = confidence
    return cfg