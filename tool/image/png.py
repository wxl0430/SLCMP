import pygame
import os

class PNGError(Exception):
    pass

cwd = os.getcwd()+"/"

def load_png(path : str,hascwd : bool = False) -> pygame.Surface:
    if not hascwd:
        path=cwd+path
    try:
        png=pygame.image.load(path)
        return png
    except:
        raise PNGError("图片"+path+"文件未找到或加载失败")
