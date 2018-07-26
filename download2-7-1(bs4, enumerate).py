import sys
import io
import urllib.request as req
from bs4 import BeautifulSoup as bs


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://finance.daum.net/index.daum?nil_profile=title&nil_src=stock"
savepath = "C:/mypy/test.html"

par = req.urlopen(url).read()
#with open(savepath, 'wb') as saveFile:
#    saveFile.write(par)

soup = bs(par, 'html.parser')

list1 = soup.select("#topMyListNo1 > li")

for i, st in enumerate(list1[0:10]):
    print(i+1, st.find('a').string,', ',st.find('span').string)
