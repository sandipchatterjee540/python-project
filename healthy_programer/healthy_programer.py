#9am-5pm
#water - water.mp3 (3.5 li) - drag -log
#eyes - eyes.mp3 - every 30 mins - eydone
#yoga - yoga.mp3 - 45mins - exdone

from time import time
from pygame import mixer
import datetime

def sound(filename,put):
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()
    while True:
        s = input("Please give input = ")
        if s==put:
            mixer.music.stop()
            break

def file_c(m):
    with open("log.txt","a") as f:
        s = f.write(f"{datetime.now()} : {m}\n")
        print(s)
        


if __name__=="__main__":
    water_t=time()
    eyes_t=time()
    yoga_t=time()
    wd=5
    ed=10
    yd=15
    while True:
        if time() - water_t > wd:
            sound("water.mp3","stop")
            file_c("drink water")
        if time() - eyes_t > ed:
            sound("eyes.mp3","stop")
            file_c("cool eyes")
        if time() -yoga_t > yd:
            sound("yoga.mp3","stop")
            file_c("go to yoga")
        break






