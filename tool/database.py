from type.touching import *
from type.node import *
from type.line import *
import json

if 'nowtouching' not in globals():
    nowtouching=Touching()

def init_database(window_settings : dict) -> None:
    global bgcolor, data, screenx, screeny, scaling, built_in_scaling, step_size, step_size_coefficient, keep_not_move_tick, mousewheel_speed
    global scaling_step_size, width, height, guide_line_scan_distance, projectsavepath, saved
    bgcolor = "#ffffff"
    data = {"node":[],"line":[]}
    width = window_settings["width"]
    height = window_settings["height"]
    screenx = int(window_settings["width"]/2)
    screeny = int(window_settings["height"]/2)
    scaling = 100
    guide_line_scan_distance = window_settings["guide_line_scan_distance"]
    built_in_scaling = int(window_settings["built_in_scaling"])
    step_size_coefficient = window_settings["step_size_coefficient"]
    step_size = int(scaling*built_in_scaling/100*step_size_coefficient)
    keep_not_move_tick = window_settings["keep_not_move_tick"]
    mousewheel_speed = window_settings["mousewheel_speed"]
    scaling_step_size  = window_settings["scaling_step_size"]
    projectsavepath = ""
    saved = True

def getsaved() -> bool:
    return saved

def setsaved(new_saved : bool) -> None:
    global saved
    saved = new_saved

def getprojectsavepath() -> str:
    return projectsavepath

def setprojectsavepath(new_path : str) -> None:
    global projectsavepath
    projectsavepath = new_path

def data_to_json_dict() -> dict:
    json_dict={"node":[],"line":[]}
    for i in data["node"]:
        json_dict["node"].append(i.tojson())
    for i in data["line"]:
        json_dict["line"].append(i.tojson())
    return json_dict

def data_from_json_dict(json_dict : dict) -> None:
    global data
    data = {"node":[],"line":[]}
    for i in json_dict["node"]:
        newnode=Node()
        newnode.fromjson(i)
        data["node"].append(newnode)
    for i in json_dict["line"]:
        newline=Line(check=False)
        newline.fromjson(i)
        data["line"].append(newline)

def inscreen(x : int, y : int) -> int:
    return 0 <= x and x <= width and 0 <= y and y <= height

def getguidelinescandistance() -> int:
    return guide_line_scan_distance

def findnodebyxy (x : int, y : int, dis : int = 5) -> Node:
    for i in data["node"]:
        if i.x-dis <= x and x <= i.x+dis and i.y-dis <= y and y <= i.y+dis:
            return i
    return None

def findnode(id : str) -> Node:
    for i in data["node"]:
        if i.id == id:
            return i
    return None

def findline(id : str) -> Line:
    for i in data["line"]:
        if i.id == id:
            return i
    return None

def getwidth() -> int:
    return width

def getheight() -> int:
    return height

def getsize() -> tuple:
    return (width, height)

def getscalingstepsize() -> int:
    return scaling_step_size

def getmousewheelspeed() -> int:
    return mousewheel_speed

def getkeepnotmovetick() -> int:
    return keep_not_move_tick

def setkeepnotmovetick(new_tick : int) -> None:
    global keep_not_move_tick
    keep_not_move_tick = new_tick

def getstepsize() -> int:
    return step_size

def setstepsize(new_step_size : int) -> None:
    global step_size
    step_size = new_step_size

def updatestepsize() -> None:
    global step_size
    step_size = int(scaling*built_in_scaling/100*step_size_coefficient)

def getscreenpos() -> tuple:
    return (screenx, screeny)

def setscreenpos(new_pos : tuple) -> None:
    global screenx, screeny
    screenx, screeny = new_pos

def movescreen(dx : int = 0, dy : int = 0) -> None:
    global screenx, screeny
    screenx += dx
    screeny += dy

def getbgcolor() -> str:
    return bgcolor

def setbgcolor(new_color : str) -> None:
    global bgcolor
    bgcolor = new_color

def newdatavalue(key : str) -> None:
    global data
    if key not in data:
        data[key] = []

def adddata(key : str, value) -> None:
    global data,saved
    saved = False
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]

def getdata() -> dict:
    return data

def deldata(key : str, idvalue) -> None:
    global data,saved
    saved = False
    if key in data:
        for i in data[key]:
            if i.id == idvalue:
                data[key].remove(i)
                break

def setdata(key : str, value) -> None:
    global data,saved
    saved = False
    data[key] = value

def setdataall(new_data : dict) -> None:
    global data,saved
    saved = False
    data = new_data

def getnowscaling() -> int:
    return scaling * built_in_scaling / 100

def setscaling(new_scaling : int) -> None:
    global scaling
    scaling = new_scaling
    updatestepsize()

def getscaling() -> int:
    return scaling

def addscaling(delta : int) -> None:
    global scaling
    scaling += delta
    updatestepsize()