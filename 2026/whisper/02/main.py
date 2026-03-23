# coding: utf-8

"""
1, Whisper
    1-1, Install
        pip install faster-whisper sounddevice scipy requests pyaudio

1, ZundaMon
    https://hub.docker.com/r/voicevox/voicevox_engine
"""

#==========
# Main

from datetime import datetime
from faster_whisper import WhisperModel
import json, pyaudio, requests

# ZUNDAMON's Host and Port
ZUNDA_HOST = "127.0.0.1"
ZUNDA_PORT = "50021"

def main():
    print("main!!")

    timestamp = get_timestamp()
    text = run_whisper(timestamp, "../sample02.mp3")
    run_zunda(timestamp, text, True)

def run_whisper(file_prefix, file_input):

    # Whisper (tiny / base / small / medium)
    model = WhisperModel("small")
    segments, _ = model.transcribe(file_input)
    text = "".join([seg.text for seg in segments])
    save_file(file_prefix + ".txt", text) # Save
    return text

def run_zunda(file_prefix, text, auto_play=False):

    # Zundamon
    params = (
        ("text", text),
        ("speaker", 3),
    )

    # Query
    query = requests.post(
        f'http://{ZUNDA_HOST}:{ZUNDA_PORT}/audio_query',
        params=params
    )

    # Synthesis
    synthesis = requests.post(
        f'http://{ZUNDA_HOST}:{ZUNDA_PORT}/synthesis',
        headers = {"Content-Type": "application/json"},
        params = params,
        data = json.dumps(query.json())
    )

    # Audio
    pya = pyaudio.PyAudio()

    # Stream
    stream = pya.open(format=pyaudio.paInt16,
        channels=1, rate=24000, output=True)
    if auto_play == True: stream.write(synthesis.content) # Play
    with open(file_prefix + ".wav", "wb") as f:
        f.write(synthesis.content)
    stream.stop_stream()
    stream.close()

    # Terminate
    pya.terminate()

def get_timestamp():
    now = datetime.now()
    text = now.strftime("%Y-%m-%d %H_%M_%S_") + f"{now.microsecond // 1000:03d}"
    return text

def save_file(file_name, text):
    file = open(file_name, "w")
    file.write(text)
    file.close();

if __name__ == "__main__":
    main()
