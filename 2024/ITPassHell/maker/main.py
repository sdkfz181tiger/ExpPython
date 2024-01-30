# coding: utf-8

"""
情報処理技術者試験_午前問ジェネレーター(ざっくり問題作成)
"""

import json, os, qrcode, random, re, sys, time
from PIL import Image, ImageFont, ImageDraw
from pathlib import Path

p_size = (2148, 3038)
p_max = p_size[1] - 300
s_pad = 160

font_40 = ImageFont.truetype("/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc", 40)
font_25 = ImageFont.truetype("/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc", 25)
credit = "= 受かる君DX_v0.99 ="

# Load
def load_questions(json_obj):
	print("load_questions")

	# Images
	images = []
	for i, piece in enumerate(json_obj["targets"]):
		# Folder, Key, Num
		folder = piece["folder"]
		key = piece["key"]
		num = piece["num"]
		# Path
		path_qs = Path(json_obj["jpg"]) / Path(folder) / Path(key+"/{:02}.jpg".format(num))
		if(not path_qs.exists()): continue
		# Title, Url, Answer
		title = json_obj["titles"][key]["title"].format(num)
		url = json_obj["titles"][key]["url"].format(num)
		answer = json_obj["answers"][key][num-1]

		# Images
		image_qs = Image.open(path_qs)
		# Title
		draw_title(image_qs, title)
		# QRCode
		draw_qrcode(image_qs, url)
		# Answer
		if(json_obj["with_answer"]): draw_answer(image_qs, answer)
		# Append
		images.append(image_qs)

	# Shuffle
	seed = json_obj["with_shuffle"]
	if(0 <= seed):
		random.seed(seed)
		random.shuffle(images)

	save_pdf(json_obj, images, "out_question.pdf")# Questions

# Save
def save_pdf(json_obj, images, name):
	print("save_pdf:", name)

	# JSON
	out_dir = Path(json_obj["out"])
	total = int(json_obj["total"]) if int(json_obj["total"]) < len(images) else len(images)

	# Positions
	p_y = 0
	p_cnt = 0

	# Pieces, Pages
	pieces = []
	pages = []

	# Number
	num = 1
	for i in range(0, total, 1):

		# Image
		image = images[i]
		w = image.size[0]
		h = image.size[1]
		
		# Number
		draw_number(image, num)# Draw number
		num += 1
		
		p_y += h + s_pad
		if(p_max < p_y):
			p_y = h + s_pad
			p_cnt = p_cnt + 1
			page = make_page(json_obj, p_cnt, pieces)
			pages.append(page)
			pieces = []# Reset
		pieces.append(image)
	
	# Last
	p_cnt = p_cnt + 1
	page = make_page(json_obj, p_cnt, pieces)
	pages.append(page)

	# Image -> PDF
	pages[0].save(out_dir / Path(name), "PDF", 
		quality=100, save_all=True, append_images=pages[1:], optimize=True)

# Draw Number
def draw_number(image, num):
	draw = ImageDraw.Draw(image) # Draw
	text = "問{:01d}".format(num)
	draw.rectangle((0, 0, 100, 70), fill=(255, 255, 255))
	draw.text((5, 0), text, font=font_40, fill=(0, 0, 0), anchor="lt")

# Draw Title
def draw_title(image, text):
	w = image.size[0]
	h = image.size[1]
	draw = ImageDraw.Draw(image) # Draw
	draw.text((w-5, h-5), text, font=font_25, fill=(0, 0, 0), anchor="rb")

# Draw QRCode
def draw_qrcode(image, url):
	qr = qrcode.QRCode(
		version=3, box_size=3, border=0,
		error_correction=qrcode.constants.ERROR_CORRECT_L
	)
	qr.add_data(url)
	qr.make(fit=True)
	image_qr = qr.make_image(fill_color="black", back_color="white").convert('L')
	image.paste(image_qr, (image.size[0]-100, 0))

# Draw Answer
def draw_answer(image, answer):
	w = image.size[0]
	h = image.size[1]
	draw = ImageDraw.Draw(image) # Draw
	draw.text((5, h-5), answer, font=font_40, fill=(0, 0, 0), anchor="lb")

# Draw Credit
def draw_credit(image):
	w = image.size[0]
	h = image.size[1]
	draw = ImageDraw.Draw(image) # Draw
	draw.text((w/2, h-20), credit, font=font_25, fill=(0, 0, 0), anchor="mb")

# Make
def make_page(json_obj, p_cnt, pieces):
	print("make_page:", p_cnt, len(pieces))

	image = Image.new("RGB", p_size, color=(255, 255, 255))

	# Credit
	draw_credit(image)

	p_x = 150
	p_y = 300
	for i, piece in enumerate(pieces):
		w = piece.size[0]
		h = piece.size[1]
		image.paste(piece, (p_x, p_y))
		p_y += h + s_pad

	return image

# Main
def main():
	# JSON
	with open("./my_data.json") as f:
		json_obj = json.load(f)
		load_questions(json_obj)

if __name__ == "__main__":
	main()