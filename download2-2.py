import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


imgUrl = "http://imgnews.naver.net/image/5129/2015/06/10/1433903908_921242_99_20150610114006.jpg"
htmlUrl = "http://google.com"

savePath1 = "c:/mypy/test.jpg"
savePath2 = "c:/mypy/test1.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlUrl).read()

saveFile1 = open(savePath1,'wb')
saveFile1.write(f)
saveFile1.close()


with open(savePath2, 'wb') as savePath2:
    savePath2.write(f2)


print("다운완료")
