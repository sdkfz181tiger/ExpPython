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
            "content": [
                {
                    "type": "text",
                    "text": "お久しぶりです、シャア少佐。あ、いや、今は大佐でいらっしゃいましたな",
                    "annotations": [{
                        "type": "speech_metadata",
                        "speaker": "Doren",
                        "style": "恐縮しながら",
                    }],
                },{
                    "type": "text",
                    "text": "相変わらずだな、ドレン",
                    "annotations": [{
                        "type": "speech_metadata",
                        "speaker": "Char",
                        "style": "落ち着き、冷静に",
                    }],
                },{
                    "type": "text",
                    "text": "はっ!!",
                    "annotations": [{
                        "type": "speech_metadata",
                        "speaker": "Doren",
                        "style": "恐縮しながら",
                    }],
                },{
                    "type": "text",
                    "text": "木馬を追っている。ちょうどお前の艦隊の位置なら木馬の頭を押さえられる",
                    "annotations": [{
                        "type": "speech_metadata",
                        "speaker": "Char",
                        "style": "落ち着き、冷静に",
                    }],
                },{
                    "type": "text",
                    "text": "ご縁がありますな、木馬とは。わかりました。追いつけますか？",
                    "annotations": [{
                        "type": "speech_metadata",
                        "speaker": "Doren",
                        "style": "恐縮しながら",
                    }],
                },{
                    "type": "text",
                    "text": "ドレン、私を誰だと思っているのだ？",
                    "annotations": [{
                        "type": "speech_metadata",
                        "speaker": "Char",
                        "style": "落ち着き、冷静に",
                    }],
                },{
                    "type": "text",
                    "text": "申し訳ありません、大佐",
                    "annotations": [{
                        "type": "speech_metadata",
                        "speaker": "Doren",
                        "style": "恐縮しながら",
                    }],
                },
            ],
        }],
        response_format={"type": "audio"},
        generation_config={
            "speech_config": {
                "mode": "conversational",
                "speakers": [
                    {"speaker": "Doren", "voice": "Puck"},
                    {"speaker": "Char", "voice": "Kore"},
                ],
            }
        },
    )

    with open("out.wav", "wb") as f:
        f.write(base64.b64decode(interaction.output_audio.data))


if __name__ == "__main__":
    main()