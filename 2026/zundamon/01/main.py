# coding: utf-8

"""
0, Official
    https://hub.docker.com/r/voicevox/voicevox_engine

1, Docker
    1-1, Download DockerDesktop and Install
        https://docs.docker.com/desktop/release-notes/
    1-2, Run DockerDesktop
        Launch DockerDesktop!!
    1-3, Check version
        docker -v
        
2, Zundamon
    2-1, Download Engine and Run
        docker pull voicevox/voicevox_engine:cpu-ubuntu20.04-latest
        docker run --rm -it -p '127.0.0.1:50021:50021' voicevox/voicevox_engine:cpu-ubuntu20.04-latest
    2-2, Install
        $ brew install portaudio
        $ python3 -m pip install pyaudio
        $ python3 -m pip install requests
"""

#==========
# Main

import json, pyaudio, requests

def main():
    print("main!!")

    # Host and Port
    host = "127.0.0.1"
    port = "50021"

    # Zundamon
    params = (
        ("text", "\
            人類が、増えすぎた人口を宇宙に移民させるようになって、既に半世紀が過ぎていた。\
            地球の周りの巨大な人工都市は、人類の第二の故郷となり、\
            人々はそこで子を産み、育て、そして死んでいった。\
            宇宙世紀ダブルオーセブンティーナイン、\
            地球から最も遠い宇宙都市、サイドスリーはジオン公国を名乗り、\
            地球連邦政府に独立戦争を挑んできた。\
            この一ヶ月あまりの戦いで、ジオン公国と連邦軍は、総人口の半分を死に至らしめた。\
            人々は、みずからの行為に恐怖した。\
            戦争は膠着状態に入り、八ヶ月あまりが過ぎたのだ!!"),
        ("speaker", 3),
    )

    # Query
    query = requests.post(
        f'http://{host}:{port}/audio_query',
        params=params
    )

    # Synthesis
    synthesis = requests.post(
        f'http://{host}:{port}/synthesis',
        headers = {"Content-Type": "application/json"},
        params = params,
        data = json.dumps(query.json())
    )

    # Audio
    pya = pyaudio.PyAudio()

    # Stream
    stream = pya.open(format=pyaudio.paInt16,
        channels=1, rate=24000, output=True)
    stream.write(synthesis.content)
    stream.stop_stream()
    stream.close()

    pya.terminate()

if __name__ == "__main__":
    main()
