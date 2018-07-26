
import sys
import io
import urllib.request as req
from bs4 import BeautifulSoup as bs


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://finance.naver.com/sise/"
#savepath = "C:/mypy/test.html"

par = req.urlopen(url).read()
#with open(savepath, 'wb') as saveFile:
#    saveFile.write(par)
soup = bs(par, 'html.parser')

list = soup.select("#siselist_tab_0 > tr")

for e in list:
    if e.find("a") is not None:
        print(e.find("a").string)


#siselist_tab_0 > tbody > tr:nth-child(3) > td:nth-child(4) > a
