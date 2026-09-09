from faster_whisper import WhisperModel

import config

_model = None


def _get_model():
    global _model
    if _model is None:
        _model = WhisperModel(
            config.WHISPER_MODEL,
            device="cpu",
            compute_type=config.WHISPER_COMPUTE_TYPE,
        )
    return _model


def transcribe(audio):
    """audio: float32 numpy array at config.SAMPLE_RATE, mono."""
    model = _get_model()
    segments, _ = model.transcribe(audio, language="en")
    text = " ".join(segment.text.strip() for segment in segments)
    return text.strip()
