# coding: utf-8

#==========
# Main

import glob
import os
import re
import urllib.request
from pathlib import Path

articles_from = "./articles_from/"
dir_images = "./images/articles/"

def main():
    print("main!!")

    files = glob.glob(articles_from + "*")
    for path_file in files:
        print("path_file:", path_file)
        urls = get_urls(path_file)
        dir_dst = dir_images + Path(path_file).stem
        download_images(urls, dir_dst)

def get_urls(path):

    # png and gif
    with open(path) as f:
        text = f.read()
        urls = re.findall(r'\((https?://[^\)]+\.gif)\)', text)
        return urls
    return None

def download_images(urls, dir_dst):

    print("urls:", urls)
    os.makedirs(dir_dst, exist_ok=True)
    for url in urls:
        print("url:", url)
        download_file(url, dir_dst)

def download_file(url, dir_dst):

    with urllib.request.urlopen(url) as f:
        dst_path = dir_dst + "/" + Path(url).name
        with open(dst_path, 'wb') as local_file:
            local_file.write(f.read())


if __name__ == "__main__":
    main()


