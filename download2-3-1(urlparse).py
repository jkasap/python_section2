import urllib.request as req
from urllib.parse import urlparse

url = "http://www.encar.com"

mem = req.urlopen(url)

#print(type(mem))
'''
print("geturl", mem.geturl())
print("status", mem.status)
print("headers", mem.headers)
'''

#print("read", mem.read(50).decode("utf-8"))

print(urlparse("http://www.encar.com"))
