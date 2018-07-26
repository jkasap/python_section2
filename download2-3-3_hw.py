import urllib.request as req
from urllib.parse import urlencode

API = "http://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"
values = {'ctxCd':'1001'}

params = urlencode(values)
reqUrl = API + "?" + params
savePath = "c:/mypy/test.txt"

reqData = req.urlopen(reqUrl).read()
with open(savePath,'wb') as saveFile:
    saveFile.write(reqData)
