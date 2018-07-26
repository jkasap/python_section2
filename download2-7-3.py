import sys
import io
import urllib.request as req
from bs4 import BeautifulSoup as bs


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.inflearn.com/"
#savepath = "C:/mypy/test.html"

par = req.urlopen(url).read()
#with open(savepath, 'wb') as saveFile:
#    saveFile.write(par)
soup = bs(par, 'html.parser')


recommand = soup.select("ul.grid")[2]
print(recommand)

for i in recommand:
    print(i.select_one("h4.block_title > a").string)
