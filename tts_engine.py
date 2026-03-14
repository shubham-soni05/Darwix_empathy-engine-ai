import os
import uuid
import asyncio

AUDIO_DIR = os.path.join("static", "audio")
os.makedirs(AUDIO_DIR, exist_ok=True)

VOICE = "en-IN-NeerjaNeural"

EMOTION_PARAMS = {
    "joy":      {"rate": "+25%", "pitch": "+8Hz"},
    "surprise": {"rate": "+30%", "pitch": "+10Hz"},
    "anger":    {"rate": "+15%", "pitch": "-5Hz"},
    "fear":     {"rate": "-20%", "pitch": "+3Hz"},
    "sadness":  {"rate": "-25%", "pitch": "-8Hz"},
    "disgust":  {"rate": "-10%", "pitch": "-5Hz"},
    "neutral":  {"rate": "+0%",  "pitch": "+0Hz"},
}

async def _synthesize(text, path, rate, pitch):
    import edge_tts
    communicate = edge_tts.Communicate(text=text, voice=VOICE, rate=rate, pitch=pitch)
    await communicate.save(path)

def _run(coro):
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None
    if loop and loop.is_running():
        import concurrent.futures
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            return pool.submit(asyncio.run, coro).result()
    else:
        return asyncio.run(coro)

def generate_speech(text: str, voice_config: dict) -> str:
    emotion    = voice_config.get("emotion", "neutral")
    params     = EMOTION_PARAMS.get(emotion, EMOTION_PARAMS["neutral"])
    final_name = f"audio/output_{uuid.uuid4().hex[:8]}.mp3"
    final_path = os.path.join("static", final_name)
    print(f"[TTS] voice={VOICE}  emotion={emotion}  rate={params['rate']}  pitch={params['pitch']}")
    _run(_synthesize(text, final_path, params["rate"], params["pitch"]))
    print(f"[TTS] Saved → {final_path}")
    return final_name