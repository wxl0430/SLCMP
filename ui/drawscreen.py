import pygame
from tool.database import *
from tool.xyconverter import *
from tool.color import *

def init_draw():
    global horizontallinenode, verticallinenode
    horizontallinenode = None
    verticallinenode = None

class DrawError(Exception):
    pass

def getHVxy() -> tuple:
    nowxy = screenxytodatabasexy(*pygame.mouse.get_pos())
    if horizontallinenode and verticallinenode:
        return (verticallinenode.x,horizontallinenode.y)
    elif horizontallinenode:
        return (nowxy[0],horizontallinenode.y)
    elif verticallinenode:
        return (verticallinenode.x,nowxy[1])
    else:
        return nowxy
    
def drawallnodes(screen : pygame.Surface) -> None:
    nowscaling = getnowscaling()
    nowdata = getdata()
    try:
        for i in nowdata["node"]:
            x, y = databasexytoscreenxy(i.x, i.y)
            pygame.draw.circle(screen, (0, 0, 0), (x, y), nowscaling)
    except:
        raise DrawError("尝试绘制节点时出错")
    try:
        if nowtouching.type == "NewNode":
            nowmouseops=pygame.mouse.get_pos()
            if horizontallinenode and verticallinenode:
                pygame.draw.circle(screen, (0, 0, 0), databasexytoscreenxy(verticallinenode.x, horizontallinenode.y), nowscaling)
            elif horizontallinenode:
                pygame.draw.circle(screen, (0, 0, 0), (nowmouseops[0], databasexytoscreenxy(0, horizontallinenode.y)[1]), nowscaling)
            elif verticallinenode:
                pygame.draw.circle(screen, (0, 0, 0), (databasexytoscreenxy(verticallinenode.x, 0)[0], nowmouseops[1]), nowscaling)                
            else:
                pygame.draw.circle(screen, (0, 0, 0), nowmouseops, nowscaling)
    except:
        raise DrawError("尝试绘制临时指示点时出错")

def drawalllines(screen : pygame.Surface) -> None:
    nowscaling = getnowscaling()
    nowdata = getdata()
    # try:
    for i in nowdata["line"]:
        node1 = findnode(i.from_id)
        node2 = findnode(i.to_id)
        x1, y1 = databasexytoscreenxy(node1.x, node1.y)
        x2, y2 = databasexytoscreenxy(node2.x, node2.y)
        x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
        pygame.draw.line(screen, hex_to_rgb(i.color), (x1, y1), (x2, y2), max(1,int(i.width*nowscaling/10)))
    # except:
    #     raise DrawError("尝试绘制直线时出错")
    try:
        if nowtouching.type == "NewLine":
            if "from_id" in nowtouching.args:
                nowmouseops=pygame.mouse.get_pos()
                node = findnode(nowtouching.args["from_id"])
                x1, y1 = databasexytoscreenxy(node.x, node.y)
                x2, y2 = nowmouseops
                pygame.draw.line(screen, (0,0,0), (x1, y1), (x2, y2), max(1,int(0.5*nowscaling)))
    except:
        raise DrawError("尝试绘制临时指示线时出错")
    
def drawguideline(screen : pygame.Surface) -> None:
    global horizontallinenode, verticallinenode
    if nowtouching.type == "NewNode":
        try:
            horizontalliney = 0
            horizontallinenode = None
            verticallinex = 0
            verticallinenode = None
            nowGLSD=getguidelinescandistance()
            # nowscaling = getnowscaling()
            nowx,nowy = pygame.mouse.get_pos()
            nowdata = getdata()
            for i in nowdata["node"]:
                x, y = databasexytoscreenxy(i.x, i.y)
                if abs(x-nowx) < abs(nowx-verticallinex):
                    verticallinex = x
                    verticallinenode = i
                if abs(y-nowy) < abs(nowy-horizontalliney):
                    horizontalliney = y
                    horizontallinenode = i
        except:
            raise DrawError("尝试计算辅助线时出错")
        try:
            if abs(nowx-verticallinex) < nowGLSD and verticallinenode and inscreen(*databasexytoscreenxy(verticallinenode.x, verticallinenode.y)):
                pygame.draw.line(screen, (0, 0, 0), (verticallinex, 0), (verticallinex, getheight()), 3)
            else:
                verticallinenode = None
            if abs(nowy-horizontalliney) < nowGLSD and horizontallinenode and inscreen(*databasexytoscreenxy(horizontallinenode.x, horizontallinenode.y)):
                pygame.draw.line(screen, (0, 0, 0), (0, horizontalliney), (getwidth(), horizontalliney), 3)
            else:
                horizontallinenode = None
        except:
            raise DrawError("尝试绘制辅助线时出错")
    else:
        horizontallinenode = None
        verticallinenode = None