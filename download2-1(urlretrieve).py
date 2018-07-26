import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


imgUrl = "http://imgnews.naver.net/image/5129/2015/06/10/1433903908_921242_99_20150610114006.jpg"
htmlUrl = "http://google.com"

savePath1 = "c:/mypy/test.jpg"
savePath2 = "c:/mypy/test1.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlUrl, savePath2)

print("다운완료")
