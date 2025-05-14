import pygame
from tool.image.png import *
from tool.xyconverter import *
import os
from file.json import *

def init_drawui():
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

def drawtext(screen,text : str,x : int,y : int,size : int,color : tuple,topplace : str = "center") -> None:
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if topplace == "center":
        text_rect.center = (x, y)
    elif topplace == "topleft":
        text_rect.topleft = (x, y)
    elif topplace == "topright":
        text_rect.topright = (x, y)
    screen.blit(text_surface, text_rect)

def drawalltext(screen : pygame.Surface) -> None:
    nowxy=screenxytodatabasexy(*pygame.mouse.get_pos())
    drawtext(screen,"x:"+str(nowxy[0])+" y:"+str(nowxy[1]),280,13,25,(200,200,200),"topleft")

def puttoollist(screen : pygame.Surface) -> None:
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

def drawui(screen : pygame.Surface) -> None:
    puttoollist(screen)
    drawalltext(screen)
