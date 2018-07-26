import sys
import io
import urllib.request as req
from bs4 import BeautifulSoup as bs

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://emart.ssg.com/category/main.ssg?dispCtgId=0006110000"
savePath = "c:/mypy/test.html"

response = req.urlopen(url).read()
"""
with open(savePath, 'wb') as saveFile:
    saveFile.write(response)
"""

soup = bs(response, "html.parser")

list1 = soup.select(".cunit_info > .cunit_md")
list2 = soup.select(".cunit_info > .cunit_price")
print(list1)
print(list2)


#for i in list1:
#    print(i.find('a').string)
