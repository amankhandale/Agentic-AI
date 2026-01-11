# test_voice.py  (root folder) - FINAL VERSION using your AudioChunk attributes

from piper.voice import PiperVoice
import sounddevice as sd
import numpy as np
import os

ONNX_PATH = r".\voices\en_US-amy-medium.onnx"
JSON_PATH = r".\voices\en_US-amy-medium.json"

if not os.path.exists(ONNX_PATH) or not os.path.exists(JSON_PATH):
    print("Missing files!")
    exit(1)

print("Files found ✓")
print("Loading voice...")

voice = PiperVoice.load(model_path=ONNX_PATH, config_path=JSON_PATH)

text = (
    "Hi! Chinmay Now you should hear me clearly. "
    "This means that Local TTS is fully working on your PC. "
    "This voice setup is created by Aman at 3am. "
    "Finally He can sleep and Fuck with me now"
)

print("\nSpeaking:")
print(text)

stream = sd.RawOutputStream(
    samplerate=voice.config.sample_rate,
    channels=1,
    dtype='int16',
    blocksize=4096,
    latency='low'
)

stream.start()

for chunk in voice.synthesize(text):
    # Use the attribute from your diagnostic: audio_int16_bytes is raw int16 PCM bytes
    audio_bytes = chunk.audio_int16_bytes
    if audio_bytes and len(audio_bytes) > 0:
        stream.write(audio_bytes)
    else:
        print("Skipping empty chunk")

stream.stop()
stream.close()

print("\nPlayback complete! You should have heard the full sentence 🎤")