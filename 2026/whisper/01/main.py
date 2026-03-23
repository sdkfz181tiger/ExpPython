# coding: utf-8

"""
1, Install
    1-1, Faster Whisper...
        pip install faster-whisper sounddevice scipy requests
"""

#==========
# Main

from datetime import datetime
from faster_whisper import WhisperModel

def main():
    print("main!!")

    # Whisper
    # tiny / base / small / medium
    model = WhisperModel("small")
    segments, _ = model.transcribe("../sample01.mp3")
    text = "".join([seg.text for seg in segments])
    file_name = get_timestamp() + ".txt"
    save_file(file_name, text) # Save

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
