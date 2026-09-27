import datetime
import io
import json
import mimetypes
import wave
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

    # Model
    model = "gemini-3.8-flash-lite-tts"

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text="""## Transcript:
あったまテカテカ、冴えてピッカピカ"""
                ),
            ],
        ),
    ]

    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        response_modalities=["audio"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name="Aoede"
                )
            )
        ),
    )

    audio_data = bytearray()
    mime_type = ""

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if chunk.parts is None:
            continue

        if chunk.parts[0].inline_data and chunk.parts[0].inline_data.data:
            inline_data = chunk.parts[0].inline_data
            audio_data.extend(inline_data.data)
            mime_type = inline_data.mime_type

        elif chunk.text:
            print(chunk.text)

    # Convert and Save
    if audio_data:
        data_buffer = bytes(audio_data)
        file_extension = mimetypes.guess_extension(mime_type)

        if file_extension is None:
            file_extension = ".wav"
            data_buffer = convert_to_wav(data_buffer)

        save_binary_file(
            f"{get_today()}{file_extension}",
            data_buffer,
        )


def convert_to_wav(audio_data: bytes) -> bytes:
    buf = io.BytesIO()

    with wave.open(buf, "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2) # 16-bit
        wav.setframerate(24000)
        wav.writeframes(audio_data)

    return buf.getvalue()


def parse_audio_mime_type(mime_type: str) -> tuple[int, int]:
    params = dict(part.split("=", 1) for part in mime_type.split(";")[1:])
    bits = int(mime_type.split("L", 1)[1].split(";", 1)[0])
    rate = int(params["rate"])
    return bits, rate


def get_today():
    today = datetime.datetime.today()
    return today.strftime('%Y%m%d_%H%M%S')


def save_binary_file(file_name, data):
    with open(file_name, "wb") as f:
        f.write(data)
    print(f"File saved to: {file_name}")


if __name__ == "__main__":
    main()