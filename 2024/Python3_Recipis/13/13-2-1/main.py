# coding: utf-8

"""
jsonモジュール
"""

#==========
# Main

import json

# Encode
data_dic = {
    "tokai": [
        {"pref": "aichi", "population": 100, "area": 100},
        {"pref": "mie", "population": 200, "area": 100},
        {"pref": "gifu", "population": 300, "area": 100}
    ],
    "tohoku": [
        {"pref": "aomori", "population": 100, "area": 100},
        {"pref": "akita", "population": 200, "area": 100},
        {"pref": "iwate", "population": 300, "area": 100},
        {"pref": "yamagata", "population": 400, "area": 100},
        {"pref": "miyagi", "population": 500, "area": 100},
        {"pref": "fukushima", "population": 600, "area": 100}
    ]
}
print(json.dumps(data_dic, indent=2))

"""
{
  "tokai": [
    {
      "pref": "aichi",
      "population": 100,
      "area": 100
    },
    ...
  ],
  "tohoku": [
    {
      "pref": "aomori",
      "population": 100,
      "area": 100
    },
    ...
  ]
}
"""

# Decode
data_str = ('{'
'"tokai":[{"pref":"aichi", "population":100, "area":100}],'
'"tohoku":[{"pref":"aomori", "population":100, "area":100}]'
'}')
print(json.loads(data_str))

# Read file -> Write file
with open("./input.json", mode="r") as i:
    data_str = json.load(i)
    with open("./output.json", mode="w") as o:
        json.dump(data_str, o, indent=4)