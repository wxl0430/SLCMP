class Touching:
    def __init__(self, type : str = "None",args : dict = {}) -> None:
        self.type = type
        self.args = args
    
    def tojson(self) -> dict:
        return {"type": self.type, "args": self.args}
    
    def __str__(self) -> str:
        return str(self.tojson())
    
    def __repr__(self) -> str:
        return str(self.tojson())