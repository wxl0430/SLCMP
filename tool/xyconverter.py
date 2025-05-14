from tool.database import *
"""
缩放 scaling*built_in_scaling/100 倍
0,0 对应 screenx,screeny
"""
def databasexytoscreenxy(x : int, y : int) -> tuple:
    nowscaling = getnowscaling()
    nowscreenpos = getscreenpos()
    nowx = x * nowscaling + nowscreenpos[0]
    nowy = y * nowscaling + nowscreenpos[1]
    nowx = int(nowx)
    nowy = int(nowy)
    return (nowx, nowy)

def screenxytodatabasexy(x : int, y : int) -> tuple:
    nowscaling = getnowscaling()
    nowscreenpos = getscreenpos()
    nowx = (x - nowscreenpos[0]) / nowscaling  
    nowy = (y - nowscreenpos[1]) / nowscaling
    nowx = int(nowx)
    nowy = int(nowy)
    return (nowx, nowy)