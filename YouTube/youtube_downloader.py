import pytube
import os
import subprocess


url = input("다운 받을 영상 url 입력 : ")
print("정보를 읽어오는 중...")
yt = pytube.YouTube(url) #다운 받을 동영상 지정
videos = yt.streams.all()

#다운 받을 퀄리티
for  i in range(len(videos)):
    print(i, ',', videos[i])

cNum = int(input("어떤 품질로 받을까?(0~21) : ")) #다운 받을 퀄리티 지정

down_dir = "C:/mypy/YouTube" #mp3 변환 때문에 다운 경로 고정함

print("다운로드 중...")
videos[cNum].download(down_dir) #다운로드


option = input("mp3로 변환하시려면 'Y'를 입력 : ") #mp3변환 옵션

if option == 'y':
    oriFileName = videos[cNum].default_filename
    newFileName = oriFileName + ".mp3"
    subprocess.call(['ffmpeg','-i',
    os.path.join(down_dir,oriFileName),
    os.path.join(down_dir,newFileName)
    ])
    print("완료!")
elif option == 'Y':
    oriFileName = videos[cNum].default_filename
    newFileName = oriFileName + ".mp3"
    subprocess.call(['ffmpeg','-i',
    os.path.join(down_dir,oriFileName),
    os.path.join(down_dir,newFileName)
    ])
    print("완료!")
else:
    print("완료!")
