import pygame
from tool.database import *
from type.node import *
from ui.drawscreen import *
def init_doing() -> None:
    global doinglist, undolist
    doinglist=[]
    undolist=[]

def newnode() -> None:
    nowtouching.type="NewNode"

def newnodenow() -> None:
    global doinglist,undolist
    nowxy=getHVxy()
    nownode=Node(*nowxy) 
    undolist=[]
    doinglist.append({"type":"NewNode","node":nownode})
    adddata("node",nownode)
    nowtouching.type="None"

def newline() -> None:
    nowtouching.type="NewLine"
    nowtouching.args={"count":0}

def newlinenow() -> None:
    global doinglist,undolist
    if nowtouching.args["count"]==2:
        nowline=Line(nowtouching.args["from_id"],nowtouching.args["to_id"])
        undolist=[]
        doinglist.append({"type":"NewLine","line":nowline})
        adddata("line",nowline)
        nowtouching.args={}
    nowtouching.type="None"

def adddoing(msg : dict) -> None:
    global doinglist,undolist
    doinglist.append(msg)

def undo () -> None:
    global doinglist,undolist
    if doinglist:
        if doinglist[-1]["type"]=="NewNode":
            deldata("node",doinglist[-1]["node"].id)
            undolist.append(doinglist[-1])
            del doinglist[-1]
        elif doinglist[-1]["type"]=="NewLine":
            deldata("line",doinglist[-1]["line"].id)
            undolist.append(doinglist[-1])
            del doinglist[-1]
        elif doinglist[-1]["type"]=="MoveNode":
            nowmovenode=findnode(doinglist[-1]["id"])
            nowmovenode.setxy(doinglist[-1]["fromx"],doinglist[-1]["fromy"])
            undolist.append(doinglist[-1])
            del doinglist[-1]

def redo () -> None:
    global doinglist,undolist
    if undolist:
        if undolist[-1]["type"]=="NewNode":
            adddata("node",undolist[-1]["node"])
            doinglist.append(undolist[-1])
            del undolist[-1]
        elif undolist[-1]["type"]=="NewLine":
            adddata("line",undolist[-1]["line"])
            doinglist.append(undolist[-1])
            del undolist[-1]
        elif undolist[-1]["type"]=="MoveNode":
            nowmovenode=findnode(undolist[-1]["id"])
            nowmovenode.setxy(undolist[-1]["tox"],undolist[-1]["toy"])
            doinglist.append(undolist[-1])
            del undolist[-1]