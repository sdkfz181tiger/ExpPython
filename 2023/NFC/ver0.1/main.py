# coding: utf-8

"""
1, Install libralies
	$ brew install libusb
	$ brew install libusb-dev
	$ brew install python3-usb
	$ python3 -m pip install libusb
	$ python3 -m pip install nfcpy
	$ python3 -m nfc

2, You can see these messages maybe!!
	This is the 1.0.4 version of nfcpy run in Python 3.11.5
	on macOS-11.7.10-x86_64-i386-64bit
	I'm now searching your system for contactless devices
	** found SONY RC-S380/S NFC Port-100 v1.11 at usb:020:010
	I'm not trying serial devices because you haven't told me
	-- add the option '--search-tty' to have me looking
	-- but beware that this may break other serial devs
"""

import binascii, nfc, os

class MyCardReader(object):
	def on_connect(self, tag):
		#タッチ時の処理
		print("【 Touched 】")

		#タグ情報を全て表示
		print(tag)

		#IDmのみ取得して表示
		self.idm = binascii.hexlify(tag._nfcid)
		print("IDm : " + str(self.idm))

		#特定のIDmだった場合のアクション
		if self.idm == "00000000000000":
			print("【 登録されたIDです 】")

		return True

	def read_id(self):
		clf = nfc.ContactlessFrontend('usb')
		try:
			clf.connect(rdwr={"on-connect": self.on_connect})
		finally:
			clf.close()

if __name__ == "__main__":
	cr = MyCardReader()
	while True:
		#最初に表示
		print("Please Touch")

		#タッチ待ち
		cr.read_id()

		#リリース時の処理
		print("【 Released 】")