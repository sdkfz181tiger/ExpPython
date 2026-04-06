# coding: utf-8

#==========
# Main

import pprint
import glob
from PIL import Image
from PIL.ExifTags import TAGS,GPSTAGS

url_google = "GoogleMap: https://www.google.com/maps/@{},{},18z"
url_google_pano = "GoogleMap(Pano): https://www.google.com/maps/@?api=1&map_action=pano&viewpoint={},{}&heading={}"

def main():
    print("main!!")

    files = glob.glob("./images/*")
    for path in files:
        info_zeroth, info_exif, info_gps = load_exif(path)
        print("==", path, "==")
        pprint.pprint(info_zeroth)
        pprint.pprint(info_exif)
        pprint.pprint(info_gps)

        if any(info_gps) == True:
            get_googlemap(info_gps)

def load_exif(path):
    with Image.open(path) as im:
        exif = im.getexif()
    info_zeroth = {TAGS[tag_id]: value for tag_id, value in exif.items()}
    info_exif   = {TAGS[tag_id]: value for tag_id, value in exif.get_ifd(0x8769).items()}
    info_gps    = {GPSTAGS[tag_id]: value for tag_id, value in exif.get_ifd(0x8825).items()}
    return info_zeroth, info_exif, info_gps

def get_googlemap(info_gps):
    lat = info_gps.get("GPSLatitude", None)
    lng = info_gps.get("GPSLongitude", None)
    direction = info_gps.get("GPSImgDirection", None) # 0は北, 90が東, 180が南, 270が西
    altitude = info_gps.get("GPSAltitude", None) # 海抜xm
    if lat and lng and direction and altitude:
        lat_dec = float(lat[0]) + float(lat[1])/60 + float(lat[2])/3600
        lng_dec = float(lng[0]) + float(lng[1]/60) + float(lng[2]/3600)
        print("北緯:", lat_dec, "東経:", lng_dec, "カメラ向き:", int(direction), "高度:", altitude)
        print(url_google.format(lat_dec, lng_dec))
        print(url_google_pano.format(lat_dec, lng_dec, direction))

if __name__ == "__main__":
    main()


