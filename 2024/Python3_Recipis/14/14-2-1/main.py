# coding: utf-8

"""
urllibモジュール(request)
"""

#==========
# Main

from urllib import parse, request
import json

#==========
# GET
url = "https://httpbin.org/get?hoge=a&fuga=b"

with request.urlopen(url) as f:
    print(f.getcode())# Status
    print(f.getheaders())# Header
    print(json.loads(f.read()))# Body

#==========
# POST
url = "https://httpbin.org/post?&hoge=a&fuga=b"
parsed = parse.urlparse(url)
data = parse.parse_qs(parsed.query)
encoded = json.dumps(data).encode()

with request.urlopen(url, data=encoded) as f:
    print(f.getcode())# Status
    print(f.getheaders())# Header
    print(json.loads(f.read()))# Body

#==========
# PUT(Requestクラス)
url = "https://httpbin.org/put?&hoge=a&fuga=b"
parsed = parse.urlparse(url)
data = parse.parse_qs(parsed.query)
encoded = json.dumps(data).encode()
req = request.Request(url, data=encoded, method="PUT")

with request.urlopen(req) as f:
    print(f.getcode())# Status
    print(f.getheaders())# Header
    print(json.loads(f.read()))# Body

#==========
# DELETE(Requestクラス)
url = "https://httpbin.org/delete?&hoge=a&fuga=b"
parsed = parse.urlparse(url)
data = parse.parse_qs(parsed.query)
encoded = json.dumps(data).encode()
req = request.Request(url, data=encoded, method="DELETE")

with request.urlopen(req) as f:
    print(f.getcode())# Status
    print(f.getheaders())# Header
    print(json.loads(f.read()))# Body