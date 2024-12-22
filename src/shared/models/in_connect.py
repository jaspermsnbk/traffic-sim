from typing import List
from .lane import Lane

class InConnection():
    nextId = 1
    id: str #generated hex id? 
    configStr: str
    lanes: List[Lane]
    def genId(self, num: int):
        return "0x" + hex(num)[2:].rjust(5,"0")

    def __init__(self, _configStr = "", _lanes = []):
        self.id = self.genId(self.nextId)
        InConnection.nextId += 1
        self.configStr = _configStr
        self.lanes = _lanes

    def __str__(self):
        return f"""
id: {self.id}
configStr: {self.configStr}
lanes: {self.lanes}
"""

