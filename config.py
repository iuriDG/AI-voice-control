"""
Central config. Swap values here as you move from Mac dev to Windows,
and once you have a custom-trained wake word.
"""

# --- Wake word ---
# Placeholder pretrained keyword. openWakeWord ships a few of these out of
# the box (hey_jarvis, alexa, hey_mycroft) so you get a working loop today.
# Replace with your custom-trained .onnx model path once it exists.
WAKE_WORD_MODEL = "hey_jarvis"
WAKE_WORD_THRESHOLD = 0.5

# --- Audio capture ---
SAMPLE_RATE = 16000          # required by both openWakeWord and Whisper
FRAME_MS = 80                # chunk size fed to the wake word detector
COMMAND_RECORD_SECONDS = 5   # fixed-length recording after wake word triggers
                              # (v2: replace with silence detection / VAD)

# --- Speech-to-text ---
WHISPER_MODEL = "small.en"   # good accuracy/speed balance on CPU
WHISPER_COMPUTE_TYPE = "int8"  # fastest on CPU; use "float16" if you have a GPU

# --- LLM ---
ANTHROPIC_MODEL = "claude-sonnet-5"
SYSTEM_PROMPT = (
    "You are a voice assistant running on the user's own computer. "
    "Keep replies short and conversational, since they will be spoken "
    "aloud. Avoid lists, headers, or markdown formatting."
)

# --- Text-to-speech ---
KOKORO_MODEL_PATH = "kokoro-v1.0.onnx"
KOKORO_VOICES_PATH = "voices-v1.0.bin"
KOKORO_VOICE = "af_heart"    # see Kokoro-82M/VOICES.md for the full list
KOKORO_LANG = "en-us"
