import sounddevice as sd
from kokoro_onnx import Kokoro

import config

_kokoro = None


def _get_kokoro():
    global _kokoro
    if _kokoro is None:
        _kokoro = Kokoro(config.KOKORO_MODEL_PATH, config.KOKORO_VOICES_PATH)
    return _kokoro


def speak(text: str):
    """Synthesizes text and plays it back through the default output device."""
    kokoro = _get_kokoro()
    samples, sample_rate = kokoro.create(
        text,
        voice=config.KOKORO_VOICE,
        speed=1.0,
        lang=config.KOKORO_LANG,
    )
    sd.play(samples, sample_rate)
    sd.wait()
