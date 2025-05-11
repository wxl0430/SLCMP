import pygame
from tool.image.png import *
import os
from file.json import *

def init_toollist():
    global images,imgdata,imgcwd,cwd
    cwd = os.getcwd() + "/"
    imgcwd = cwd + "image/"
    try:
        imgdata=read_json("setting/window.json")["images"]
    except:
        raise JsonFileError("window.json解析失败")
    images=[]
    for i in imgdata:
        images.append(load_png("image/"+i["name"]))
'''
(x,y)
  x->
 y
 |
\ /
'''
def puttoollist(screen):
    try:
        for i in range(len(images)):
            if imgdata[i]["display"]:
                screen.blit(images[i],(imgdata[i]["x"],imgdata[i]["y"]))
    except:
        raise JsonFileError("window.json解析失败")

def getimgdata() -> list:
    return imgdata

def setimgdata(newimgdata: list) -> None:
    global imgdata
    imgdata=newimgdata