# coding: utf-8

"""
CRON Test
"""

#==========
# Main

from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # For CRON

def main():
    print("main!!")

    text = get_timestamp() + " やぁやぁ、CRONで再起動してやったんだぜ!!\n"
    save_file("cron.log", text)

def get_timestamp():
    now = datetime.now()
    text = now.strftime("%Y-%m-%d %H_%M_%S_") + f"{now.microsecond // 1000:03d}"
    return text

def save_file(file_name, text):
    path = os.path.join(BASE_DIR, file_name)
    file = open(path, "a")
    file.write(text)
    file.close();

if __name__ == "__main__":
    main()
