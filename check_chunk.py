from piper.voice import PiperVoice

voice = PiperVoice.load(
    r".\voices\en_US-amy-medium.onnx",
    r".\voices\en_US-amy-medium.json"
)

text = "short test"

print("Generating chunks...")

first_chunk = next(voice.synthesize(text))

print("First chunk type:", type(first_chunk))
print("Chunk attributes:", dir(first_chunk))
print("Has 'audio' attribute?", hasattr(first_chunk, 'audio'))
if hasattr(first_chunk, 'audio'):
    print("Audio type:", type(first_chunk.audio))
    print("Audio length (bytes):", len(first_chunk.audio) if first_chunk.audio else 0)