import os

from anthropic import Anthropic

import config
from wake_word import WakeWordListener
from transcribe import transcribe
from speak import speak


def ask_llm(client: Anthropic, user_text: str) -> str:
    response = client.messages.create(
        model=config.ANTHROPIC_MODEL,
        max_tokens=300,
        system=config.SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_text}],
    )
    return "".join(
        block.text for block in response.content if block.type == "text"
    ).strip()


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit(
            "Set ANTHROPIC_API_KEY in your environment before running this."
        )
    client = Anthropic(api_key=api_key)

    listener = WakeWordListener()

    while True:
        listener.listen_for_wake_word()
        audio = listener.record_command()

        text = transcribe(audio)
        if not text:
            print("Didn't catch that.")
            continue
        print(f"You said: {text}")

        reply = ask_llm(client, text)
        print(f"Assistant: {reply}")

        speak(reply)


if __name__ == "__main__":
    main()
