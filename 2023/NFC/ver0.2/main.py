# coding: utf-8

from modules.nfc_manager import NFCManager

if __name__ == "__main__":
	print("Hello, NFC!!")

	# NFCManager
	nfcMng = NFCManager("./data.sqlite")
	nfcMng.startTimer()