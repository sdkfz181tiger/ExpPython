# coding: utf-8

"""
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
		$ python3 -m pip install pyaudio
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
		("text", "賛成の反対なのだ!!"),
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
