# coding: utf-8

from modules.nfc_manager import NFCManager
from modules.ui_manager import UIManager

if __name__ == "__main__":
	print("Hello, NFC!!")

	def on_start():
		print("Start")
		nfcMng.startNFC()

	def on_stop():
		print("Stop")

	# NFCManager
	nfcMng = NFCManager("./data.sqlite")

	# UIManager
	uiManager = UIManager(on_start, on_stop)

