# coding: utf-8

#==========
# Main

import requests
import xml.etree.ElementTree as ET

url_itmedia = "https://rss.itmedia.co.jp/rss/2.0/kw_akiba.xml"

def main():
    print("main!!")

    # Request
    res = requests.get(url_itmedia)
    # Parse
    parse_rss(res.content)

def parse_rss(text):

    # Parse
    root = ET.fromstring(text)

    # Channel
    channel = root.find("channel")
    title = channel.find("title").text
    pub_date = channel.find("pubDate").text

    # Items
    items = channel.findall("item")
    for item in items:
        title = item.find("title").text
        description = item.find("description").text
        link = item.find("link").text
        pub_date = item.find("pubDate").text
        print(title, description, link, pub_date)
    
if __name__ == "__main__":
    main()


