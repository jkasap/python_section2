import urllib.request as ur

imgUrl = "http://ojsfile.ohmynews.com/PHT_IMG_FILE/2017/0811/IE002202038_PHT.jpg"

savePath1 = "C:/mypy/test1.png"

#ur.urlretrieve(imgUrl, savePath1)
f = ur.urlopen(imgUrl).read()
'''
saveFile1 = open(savePath1,'wb')
saveFile1.write(f)
saveFile1.close()
'''

with open(savePath1, 'wb') as saveFile1:
    saveFile1.write(f)

print('done')
