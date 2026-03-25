# coding: utf-8

"""
CRON Test
"""

#==========
# Main

from datetime import datetime
import json
import os
import requests
import subprocess
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # For CRON

def main():
    print("main!!")

    time.sleep(2) # 2sec

    # JSON
    response = requests.get("http://arduino-sensor.local/sensors")
    json_data = response.json()

    text = datetime.now().strftime("ただいま、%m月%d日、%H時%M分です。")
    text += "気温は{}度、".format(json_data["temp"])
    text += "湿度は{}%、".format(json_data["hum"])
    text += "気圧は{}ヘクトパスカル、".format(json_data["press"]/100)
    text += "明るさは{}です。".format(json_data["light"])
    talk_yukkuri(text)
    save_log("cron.log", text)

def get_timestamp():
    now = datetime.now()
    text = now.strftime("%Y-%m-%d %H_%M_%S_") + f"{now.microsecond // 1000:03d}"
    return text

def save_log(file_name, text):
    path = os.path.join(BASE_DIR, file_name)
    file = open(path, "a")
    file.write(get_timestamp() + "_" + text + "\n")
    file.close()

def talk_yukkuri(text):
    aquestalk = "/home/kajiru/Desktop/aquestalkpi/AquesTalkPi"
    aplay = "/usr/bin/aplay"
    p1 = subprocess.Popen([aquestalk, text], stdout=subprocess.PIPE)
    #p2 = subprocess.Popen([aplay], stdin=p1.stdout) # HDMI
    p2 = subprocess.Popen([aplay, "-D", "plughw:1,0"], stdin=p1.stdout) # ヘッドフォン
    p1.stdout.close()
    p2.communicate()

if __name__ == "__main__":
    main()
