# coding: utf-8

#==========
# Main

import glob
import os
import re
import urllib.request
from pathlib import Path

articles_from = "./articles_from/"
articles_to = "./articles_to/"

def main():
    print("main!!")

    files = glob.glob(articles_from + "*")
    for path_file in files:
        print("path_file:", path_file)

        # Replace url to local path
        # https://storage.googleapis.com/zenn-user-upload/
        # /images/articles/xxx/

        replace_from = "https://storage.googleapis.com/zenn-user-upload/"
        replace_to   = "/images/articles/" + Path(path_file).stem + "/"
        print("replace_from:", replace_from)
        print("replace_to:", replace_to)

        # Directory
        os.makedirs(articles_to, exist_ok=True)

        # Read and Write
        with open(path_file) as f_read:
            text = f_read.read().replace(replace_from, replace_to)
            with open(articles_to + Path(path_file).name, mode="w") as f_write:
                f_write.write(text)

if __name__ == "__main__":
    main()


