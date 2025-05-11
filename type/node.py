from tool.id import *
import json
class Node:
    def __init__(self, x : int = 0, y : int = 0) -> None:
        self.x = x
        self.y = y
        self.id = new_id("node_")
    
    def setxy(self, sx : int, sy : int) -> None:
        self.x = sx
        self.y = sy

    def fromjson(self, json_dict : dict) -> None:
        self.id = json_dict["id"]
        self.x = json_dict["x"]
        self.y = json_dict["y"]

    def tojson(self) -> dict:
        return {"id": self.id, "x": self.x, "y": self.y}
    
    def __str__(self) -> str:
        return str(self.tojson())
    
    def __repr__(self) -> str:
        return str(self.tojson())