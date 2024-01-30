# coding: utf-8

"""
情報処理技術者試験_午前問ジェネレーター(ざっくり問題切り抜き)

Tesseract
	1, Install
		brew install tesseract
		python3 -m pip install pytesseract
	2, Download train data(2 files)
		https://github.com/tesseract-ocr/tessdata_best
			jpn.traineddata
			jpn_vert.traineddata
	3, Add train data(2 files)
		brew list tesseract
			...
			/usr/local/Cellar/tesseract/5.3.2/share/tessdata/ (35 files)
	4, Check
		print(pytesseract.get_languages())
			['eng', 'jpn', 'jpn_vert', 'osd', 'snum']

PDF
	1, Install
		brew install poppler
		python3 -m pip install pdf2image
		python3 -m pip install pyocr
"""

import json
from modules.pdf_cropper import PdfCropper

# Main
def main():
	print("main")

	# JSON
	with open("./my_data_to.json") as f:
		json_obj = json.load(f)
		for data in json_obj["data"]:
			# PdfCropper
			pdf     = data["pdf"]
			jpg     = data["jpg"]
			title   = data["title"]
			active  = data["active"]
			if(not active): continue
			print("Active:", title)
			pCropper= PdfCropper(pdf=pdf, jpg=jpg, title=title)
			pCropper.pdf2image()

if __name__ == "__main__":
	main()