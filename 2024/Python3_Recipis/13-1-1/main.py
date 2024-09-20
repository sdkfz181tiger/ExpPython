# coding: utf-8

"""
csvモジュール
"""

#==========
# Main

import csv

# CSV
with open("input.csv", mode="r", encoding="utf-8") as f:
    for row in csv.reader(f):
        print(row)

"""
['pref', 'population', 'area']
['aomori', '1184531', '9645.10']
['akita', '913556', '11637.52']
['iwate', '1163024', '15275.04']
['yamagata', '1026228', '9323.15']
['miyagi', '2263552', '7282.29']
['fukushima', '1766358', '13784.39']
"""

# DictReader
with open("input.csv", mode="r", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row)

"""
{'pref': 'aomori', 'population': '1184531', 'area': '9645.10'}
{'pref': 'akita', 'population': '913556', 'area': '11637.52'}
{'pref': 'iwate', 'population': '1163024', 'area': '15275.04'}
{'pref': 'yamagata', 'population': '1026228', 'area': '9323.15'}
{'pref': 'miyagi', 'population': '2263552', 'area': '7282.29'}
{'pref': 'fukushima', 'population': '1766358', 'area': '13784.39'}
"""

# DictWriter
data = [
    {"pref": "Aichi", "population": 7480897, "area": 5173.19},
    {"pref": "Mie", "population": 1727503, "area": 5774.48},
    {"pref": "Gifu", "population": 1929669, "area": 10621.29}
]

with open("output.csv", newline="", mode="w", encoding="utf-8") as f:
    names = ["pref", "population", "area"]
    writer = csv.DictWriter(f, fieldnames=names)
    writer.writeheader()
    writer.writerows(data)