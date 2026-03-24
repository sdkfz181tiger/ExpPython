# coding: utf-8

"""
CRON Test
"""

#==========
# Main

import subprocess
import time

def main():
    print("main!!")

    time.sleep(10)

    aquestalk = "/home/kajiru/Desktop/aquestalkpi/AquesTalkPi"
    aplay = "/usr/bin/aplay"
    text = "こんにちは、ゆっくりれいむと、ゆっくりまりさだぜ"

    p1 = subprocess.Popen([aquestalk, text], stdout=subprocess.PIPE)
    p2 = subprocess.Popen([aplay], stdin=p1.stdout)

    p1.stdout.close()
    p2.communicate()

if __name__ == "__main__":
    main()
