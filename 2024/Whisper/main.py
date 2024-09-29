# coding: utf-8

"""
1, Venv

    1-1, New
        $cd [project dir]
        $python3 -m venv [newenvname]

    1-2, Activate
        $source [newenvname]/bin/activate

    1-3, Check
        $python3 -V

    1-4, Upgrade
        $python3 -m pip install --upgrade pip

    1-5, Check
        $python3 -m pip -V

    1-6, Deactiate
        $deactivate

2, ffmpeg

    2-1, install
        $brew install ffmpeg

3, Whisper: https://github.com/openai/whisper

    3-1,
        $python3 -m pip install -U openai-whisper

    3-2, Check
        $python3 -m pip list
"""

#==========
# Main

import whisper

def main():
    print("main!!")

    # Model(tyny, base, small, medium, large)
    model = whisper.load_model("medium")

    # File
    file_input = "./sample.mp3"
    file_output = "./output.mp3"

    result = model.transcribe(file_input, verbose=True, language="ja")
    print(result["text"])

if __name__ == "__main__":
    main()
