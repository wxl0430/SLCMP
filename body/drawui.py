import pygame
from tool.image.png import *
from tool.xyconverter import *
from tool.stringconverter import *
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

def drawtext(screen, text : str, x : int, y : int, size : int, color : tuple, topplace : str = "center",fontname : str = "Consolas") -> None:
    font = pygame.font.SysFont(fontname, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if topplace == "center":
        text_rect.center = (x, y)
    elif topplace == "topleft":
        text_rect.topleft = (x, y)
    elif topplace == "topright":
        text_rect.topright = (x, y)
    elif topplace == "bottomleft":
        text_rect.bottomleft = (x, y)
    elif topplace == "bottomright":
        text_rect.bottomright = (x, y)
    screen.blit(text_surface, text_rect)

def drawalltext(screen : pygame.Surface) -> None:
    nowxy=screenxytodatabasexy(*pygame.mouse.get_pos())
    drawtext(screen,
             "x:"+stringsetlength(str(int(nowxy[0])),6)+
             "|y:"+stringsetlength(str(int(nowxy[1])),6)+
             "|SC:"+stringsetlength(str(int(getscaling()))+"%",6)+
             "|SX:"+stringsetlength(str(getscreenpos()[0]),6)+
             "|SY:"+stringsetlength(str(getscreenpos()[1]),6)
             ,1795,1000,20,(160,160,160),"bottomright")

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
