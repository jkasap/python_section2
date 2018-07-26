import sys
import io
import urllib.request as req
import urllib.parse as rep
from bs4 import BeautifulSoup as bs
import os


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("정연")
tem_url = base + quote

#403 금지 해결
url = req.Request(tem_url, headers={'User-Agent' : 'Mozilla/5.0'})

res = req.urlopen(url)
savePate = "c:/mypy/img_down/"

#예외처리
try:
    if not (os.path.isdir(savePate)):
        os.makedirs(os.path.join(savePate))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        raise

soup = bs(res, "html.parser")

img_list = soup.select("div.img_area._item > a.thumb._thumb > img")

for i, img_list in enumerate(img_list,1):
    fullFileName = os.path.join(savePate, savePate+str(i)+'.jpg')
    req.urlretrieve(img_list["data-source"], fullFileName)


print("다운로드 완료")
