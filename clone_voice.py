import base64
import os
import sys

from sarvamai import SarvamAI

api_key = os.environ.get("SARVAM_API_KEY")
if not api_key:
    raise SystemExit("Set SARVAM_API_KEY in the environment before running this script.")

reference_path = sys.argv[1] if len(sys.argv) > 1 else "reference.wav"
client = SarvamAI(api_subscription_key=api_key)

with open(reference_path, "rb") as reference:
    created = client.voice_cloning.create_voice(
        file=reference,
        name="my-voice",
        language="en-IN",
    )

response = client.voice_cloning.convert(
    voice_id=created.data.voice_id,
    text="नमस्ते, मैं आपकी कैसे मदद कर सकता हूँ?",
)

with open("output.wav", "wb") as output:
    output.write(base64.b64decode(response.audio_b64 or response.audio))

print("Saved narration to output.wav")
