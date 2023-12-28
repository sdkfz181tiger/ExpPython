# coding: utf-8

"""
SpeechRecognition
1, Install
	$ python3 -m pip install speechrecognition
"""

import speech_recognition as sr

#==========
# Main

def main():
	print("main!!")

	# Recognizer
	rec = sr.Recognizer()
	with sr.AudioFile("./sample.wav") as source:
		audio = rec.record(source)

	# Result
	rec_result = rec.recognize_google(audio, language="ja-JP")
	print(rec_result)

if __name__ == "__main__":
	main()