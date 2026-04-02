# coding: utf-8

#==========
# Main

import glob
from PIL import Image

def main():
    print("main!!")

    files = glob.glob("./images/*")
    for path in files:
        with Image.open(path) as im:
            exif = im.getexif()

        exif_dict = exif.get_ifd(0x8769) # Exif情報の取得
        gps_dict = exif.get_ifd(0x8825)  # GPS情報の取得

        print("path:", path)
        print("  exif_dict:", exif_dict)
        print("  gps_dict:", gps_dict)

if __name__ == "__main__":
    main()
