# voice-agent

Milestone 1: wake word -> local transcription -> Claude -> local speech reply.
No system control yet, that's milestone 3.

Fully cross-platform. Build and test on your Mac now, then copy this folder
to Windows later with no changes needed for this part.

## Setup

1. Create a virtual environment and install dependencies:

   ```
   python3 -m venv venv
   source venv/bin/activate        # Windows later: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Download the Kokoro model files and place them in this folder:
   - `kokoro-v1.0.onnx`
   - `voices-v1.0.bin`

   Both are on the `kokoro-onnx` GitHub releases page (thewh1teagle/kokoro-onnx).

3. Set your Anthropic API key:

   ```
   export ANTHROPIC_API_KEY=sk-ant-...     # Windows later: setx ANTHROPIC_API_KEY "sk-ant-..."
   ```

4. On macOS, grant your terminal microphone access the first time you run
   this: System Settings > Privacy & Security > Microphone.

5. Run it:

   ```
   python main.py
   ```

   Say "hey jarvis" (the placeholder wake word), wait for "Listening for
   your command...", then speak. It transcribes, sends your text to Claude,
   and speaks the reply back.

## Known limitations (by design, for now)

- Wake word is a stock openWakeWord keyword, not your custom one yet.
- Command recording is a fixed 5-second window, not silence-detected. If
  you talk longer than that it'll cut you off; shorter, it'll wait around.
  Silence-based end-of-speech detection is a natural next improvement.
- No conversation memory between turns, each command is a fresh request.
- No system/computer control. That's milestone 3, once this loop feels good.

## Next steps

- Swap `WAKE_WORD_MODEL` in `config.py` for a custom-trained word once you've
  picked one and run it through openWakeWord's training notebook.
- Add silence detection to `record_command()` instead of a fixed duration.
- Add multi-turn memory (keep a running `messages` list instead of one-shot).
