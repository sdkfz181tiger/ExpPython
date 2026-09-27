import base64
import json
from google import genai
from google.genai import types


def main():
    print("main!!")

    # JSON
    with open("./settings.json") as f:
        json_obj = json.load(f)
        api_key = json_obj["api_key"]

    # Client
    client = genai.Client(api_key=api_key)

    interaction = client.interactions.create(
        model="gemini-3.8-flash-lite-tts",
        input=[{
            "type": "user_input",
            "content": [{
                "type": "text",
                "text": "燃え上がれ、燃え上がれ、燃え上がれガンダム!!",
                "annotations": [{
                    "type": "speech_metadata",
                    "style": "悲しく、辛い、絶望的に",
                }],
            }],
        }],
        response_format={"type": "audio"},
        generation_config={
            "speech_config": [
                {"voice": "Kore"},
            ]
        },
    )

    with open("out.wav", "wb") as f:
        f.write(base64.b64decode(interaction.output_audio.data))


if __name__ == "__main__":
    main()