import sys
import io
import urllib.request as req
from bs4 import BeautifulSoup as bs
import re


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.daum.net/"

par = req.urlopen(url).read()
soup = bs(par, "html.parser")

#내가 푼 것
top10 = soup.select("div.rank_cont > span.txt_issue > a")

for i in top10:
    if i.get('tabindex') == '-1':
        print(i.string, i.get('href'))


#다른 방법
top10 = soup.find_all("a", tabindex="-1")

for i, e in enumerate(top10,1):
    print(i,e.string)
