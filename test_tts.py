import soundfile as sf
from kokoro_onnx import Kokoro
import config

kokoro = Kokoro(config.KOKORO_MODEL_PATH, config.KOKORO_VOICES_PATH)
samples, sr = kokoro.create("Testing one two three", voice=config.KOKORO_VOICE, lang=config.KOKORO_LANG)
sf.write("test_output.wav", samples, sr)