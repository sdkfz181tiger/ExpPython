# coding: utf-8

"""
1, Install libraries
	$ brew install libusb
	$ brew install libusb-dev
	$ brew install python3-usb
	$ python3 -m pip install libusb
	$ python3 -m pip install nfcpy

2, Reboot <- Important!!

3, Start NFC
	$ python3 -m nfc

4, You can see these messages!!
	This is the 1.0.4 version of nfcpy run in Python 3.11.5
	on macOS-11.7.10-x86_64-i386-64bit
	...
"""

import binascii, datetime, hashlib, nfc, os, sqlite3

class NFCManager():

	def __init__(self, path_db):
		print("NFCManager")
		self.path_db = path_db
		self.wait_flg = False

	def checkData(self):
		print("checkData!!")
		# SQLite
		con = sqlite3.connect(self.path_db)
		cur = con.cursor()
		cur.execute("SELECT * FROM main")
		list = cur.fetchall()
		for record in list:
			print(record)
		con.close()

	def insertData(self, usr_idm, usr_time):
		print("insertData!!")
		# SQLite
		con = sqlite3.connect(self.path_db)
		cur = con.cursor()
		cur.execute("INSERT INTO main VALUES(?, ?, ?)", (None, usr_idm, usr_time))
		con.commit()# Important
		con.close()

	def onConnect(self, tag):
		print("onConnect:", tag)
		self.wait_flg = False
		# IDm(MD5), Time
		usr_idm = hashlib.md5(binascii.hexlify(tag._nfcid)).hexdigest()
		usr_time = datetime.datetime.now().strftime("%Y/%m/%d_%H:%M:%S")
		self.insertData(usr_idm, usr_time)# Insert
		self.checkData()# Check

	def startNFC(self):
		print("startNFC...")
		if self.wait_flg: return
		self.wait_flg = True
		# NFC
		while(self.wait_flg):
			clf = nfc.ContactlessFrontend("usb")
			try:
				clf.connect(rdwr={"on-connect": self.onConnect})
			finally:
				clf.close()