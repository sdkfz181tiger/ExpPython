# coding: utf-8

"""
情報処理技術者試験_午前問ジェネレーター(画像をトリムしてタイトルを付ける)
"""

import glob, os
from PIL import Image, ImageFont, ImageDraw
from pathlib import Path

font_25 = ImageFont.truetype("/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc", 25)

# Main
def main():
	print("main")

	title = "[IP_令x春:問{:01d}]"
	trim_from = "../assets/jpg/ip/2013h25a_ip_qs"
	#trim_from = "./jpg/from/"
	trim_to   = "./jpg/to/"

	pad_l = 0
	pad_r = 0
	pad_t = 0

	# From
	files = glob.glob(trim_from + "/*")
	for file in files:
		# Name, Num, Path
		name = os.path.split(file)[1]
		num = name.split(".")[0]
		path = Path(trim_to) / Path(name)
		print(name, num, path)

		# Images
		image = Image.open(file)
		# Size
		w = image.size[0]
		h = image.size[1]
		# Crop
		crop = image.crop((pad_l, pad_t, w-pad_r, h+30))
		# Draw
		draw = ImageDraw.Draw(crop) # Draw
		draw.rectangle(((0, h-2), (w, h+32)), fill=(255, 255, 255))
		# Title
		text = title.format(int(num))
		draw.text((w-5, h-5), text, font=font_25, fill=(0, 0, 0), anchor="rt")
		# Save
		crop.save(path, "JPEG") # Save

if __name__ == "__main__":
	main()