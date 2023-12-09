# coding: utf-8

import os, pytesseract, pyocr, re, sys, time
from PIL import Image, ImageFont, ImageDraw, ImageChops, ImageFilter
from pathlib import Path
from pdf2image import convert_from_path

# PdfCropper
class PdfCropper:

	def __init__(self, pdf, jpg, title):
		print("PdfCropper")

		# Pytesseract
		print(pytesseract.get_languages())

		# PDF
		self.pdf_path = Path(pdf)
		if(not self.pdf_path.exists()): sys.exit(1)

		# Directory
		self.jpg_dir = Path(jpg) / Path(self.pdf_path.stem)
		if(not self.jpg_dir.is_dir()): self.jpg_dir.mkdir()

		# Format
		self.title_format = title

		# Pages
		self.pdf_pages = convert_from_path(str(self.pdf_path), 300)

		# PyOCR
		self.tools = pyocr.get_available_tools() 
		if(len(self.tools) == 0): sys.exit(1)
		self.tool = self.tools[0]

		# TextBuilder  文字列を認識
		# WordBoxBuilder  単語単位で文字認識 + BoundingBox
		# LineBoxBuilder  行単位で文字認識 + BoundingBox
		# DigitBuilder  数字 / 記号を認識
		# DigitLineBoxBuilder  数字 / 記号を認識 + BoundingBox
		self.builder = pyocr.builders.LineBoxBuilder(tesseract_layout=6)

		# Font
		self.font = ImageFont.truetype("/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc", 30)

		# Poppler
		poppler_dir = Path(__file__).parent.absolute() / "poppler/bin"
		os.environ["PATH"] += os.pathsep + str(poppler_dir)
		
	# PDF -> Image
	def pdf2image(self):
		print("pdf2image...")

		# Pages
		for i, page in enumerate(self.pdf_pages):
			num = i + 1
			name = self.pdf_path.stem + "_{:02d}.jpg".format(num)
			path = self.jpg_dir / name
			if(0 < i):
				page = self.trim_top_bottom(page, num=num)
				page = self.trim_left(page, num=num)
			page.save(str(path), "JPEG") # Save
			#if(3 < i): return # For test: ページ数を限定

	# Trim
	def trim_top_bottom(self, image, num=0, thre=250, pad=30):
		print("trim_top_bottom...:", num)

		w = image.size[0]
		h = image.size[1]

		# Hide number
		draw = ImageDraw.Draw(image) # Draw
		draw.rectangle(((0, h-250), (w, h)), fill=(255, 255, 255))

		# Resize
		resizedV = image.resize((1, h))
		for t in range(h):
			p = resizedV.getpixel((0, t))
			avg = int((p[0] + p[1] + p[2]) / 3)
			if(avg < thre): break
		for b in range(h-1, 0, -1):
			p = resizedV.getpixel((0, b))
			avg = int((p[0] + p[1] + p[2]) / 3)
			if(avg < thre): break
		if(b < t):
			t = 0
			b = h
		return image.crop((0, t-pad, w, b+pad))

	# Trim(bottom)
	def trim_bottom(self, image, num=0, thre=250, pad=30):
		print("trim_bottom...:", num)

		w = image.size[0]
		h = image.size[1]

		# Resize
		resizedV = image.resize((1, h))
		for b in range(h-1, 0, -1):
			p = resizedV.getpixel((0, b))
			avg = int((p[0] + p[1] + p[2]) / 3)
			if(avg < thre): break
		return image.crop((0, 0, w, b+pad))

	# Trim left
	def trim_left(self, image, num=0, pad=30):
		print("trim_left...:", num)

		w = image.size[0]
		h = image.size[1]
		min_x = 9999
		max_x = 0
		cuts_y = [0]
		draw = ImageDraw.Draw(image) # Draw

		# Image -> String
		result = self.tool.image_to_string(image, lang="jpn", builder=self.builder)

		for d in result:
			if(self.check_text(d.content)): continue
			x = d.position[0][0]
			if(x < min_x): min_x = x
			if(max_x < x): max_x = x
			cuts_y.append(d.position[0][1]) # Cut position y
			#draw.rectangle(d.position, outline=(255, 0, 0), width=2) # For test: 認識部分をハイライト
		if(w <= min_x): min_x = 0
		if(max_x <= 0): max_x = w
		cuts_y.append(h)

		# Image -> Pieces
		if 0 < len(result): self.cut2pieces(image, num, min_x-pad, cuts_y)

		return image.crop((min_x-pad, 0, w, h))

	# Check text
	def check_text(self, text):
		print("check_text...", text)
		if(re.search("^\s*注\s*意\s*事\s*項", text)): return True
		if(re.search("^\s*(問|間)\s*\d+\s*か\s*ら", text)): return True
		if(not re.search("^・*\s*(問|間)\s*\d+\s*", text)): return True
		return False

	# Cut
	def cut2pieces(self, image, num, x, cuts_y):
		print("cut2pieces...: num:{0}_cuts_y:{1}".format(num, len(cuts_y)))

		w = image.size[0]
		h = image.size[1]
		for i, y in enumerate(cuts_y):
			if(h <= y): break
			name = self.pdf_path.stem + "_{0:02d}_{1:02d}.jpg".format(num, i+1)
			path = self.jpg_dir / name
			piece = image.crop((x, y, w, cuts_y[i + 1]))
			piece = self.trim_bottom(piece)
			piece.save(str(path), "JPEG") # Save