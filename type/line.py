from tool.id import *
import json
class NewLineError(Exception):
    pass

class Line:
    def __init__(self, from_id : str = None, to_id : str = None, color : str = "#000000", width : int = 5, check : bool = True) -> None:
        if check:
            if not check_id(from_id):
                raise NewLineError("未找到起始节点，创建失败")
            if not check_id(to_id): 
                raise NewLineError("未找到终止节点，创建失败")
        self.from_id = from_id
        self.to_id = to_id
        self.color = color
        self.width = width
        self.id = new_id("line_")
    
    def fromjson(self,json_dict : dict) -> None:
        self.id = json_dict["id"]
        self.from_id = json_dict["from_id"]
        self.to_id = json_dict["to_id"]
        self.color = json_dict["color"]
        self.width = json_dict["width"]
    
    def tojson(self) -> dict:
        return {"id": self.id, "from_id": self.from_id, "to_id": self.to_id, "color": self.color, "width": self.width}
    
    def __str__(self) -> str:
        return str(self.tojson())
    
    def __repr__(self) -> str:
        return str(self.tojson())