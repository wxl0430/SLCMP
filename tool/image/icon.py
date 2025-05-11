import pygame
import os

class IconError(Exception):
    pass

cwd = os.getcwd()+"/"

def load_icon(path : str,hascwd : bool = False) -> pygame.Surface:
    if not hascwd:
        path=cwd+path
    try:
        icon=pygame.image.load(path)
        return icon
    except:
        raise IconError("图标文件未找到或加载失败")
