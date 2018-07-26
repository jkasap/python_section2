import urllib.request as ur

url ="https://ssl.pstatic.net/tveta/libs/1205/1205488/b286bbd6dc5769c39dc3_20180720181318205.png"
savepath = "c:/mypy/test.jpg"


data = ur.urlopen(url).read()
with open(savepath,'wb') as sf:
    sf.write(data)
