import numpy as np
import sounddevice as sd
from openwakeword.model import Model

import config


class WakeWordListener:
    """
    Streams mic audio and blocks until the configured wake word fires.
    Call listen_for_wake_word() in a loop.
    """

    def __init__(self):
        self.model = Model(wakeword_models=[config.WAKE_WORD_MODEL])
        self.frame_samples = int(config.SAMPLE_RATE * config.FRAME_MS / 1000)

    def listen_for_wake_word(self):
        print(f"Listening for wake word ({config.WAKE_WORD_MODEL})...")
        with sd.InputStream(
            samplerate=config.SAMPLE_RATE,
            channels=1,
            dtype="int16",
            blocksize=self.frame_samples,
        ) as stream:
            while True:
                frame, _ = stream.read(self.frame_samples)
                frame = frame.flatten()
                predictions = self.model.predict(frame)
                score = predictions.get(config.WAKE_WORD_MODEL, 0.0)
                if score > config.WAKE_WORD_THRESHOLD:
                    self.model.reset()
                    return

    def record_command(self, seconds=None):
        """Records a fixed window of audio right after the wake word fires."""
        seconds = seconds or config.COMMAND_RECORD_SECONDS
        print("Listening for your command...")
        audio = sd.rec(
            int(seconds * config.SAMPLE_RATE),
            samplerate=config.SAMPLE_RATE,
            channels=1,
            dtype="float32",
        )
        sd.wait()
        return audio.flatten()
