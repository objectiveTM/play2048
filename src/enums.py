from enum import Enum
from .custom import *

class move(Enum):
    UP    = "up"
    DOWN  = "down"
    LEFT  = "left"
    RIGHT = "right"
    def __str__(self) -> str:
        return self.value
    
    def __add__(self, a:str):
        if a.lower() == "up":return self.UP
        elif a.lower() == "down":return self.DOWN
        elif a.lower() == "left":return self.LEFT
        elif a.lower() == "right":return self.RIGHT
        else: return self.value
    
    def __radd__(self, a:str):
        return self.__add__(a)

class customs(Enum):
    ORIGINAL = Custom(
        bg="#BBADA0", 
        none = "#F9CF00", 
        font = "#F9F6F2", 
        _0 = "#CCC0B3",
        _2 = "#EEE4DA",
        _4 = "#EEE1C9",
        _8 = "#F3B27A",
        _16 = "#F69664",
        _32 = "#F77C5F",
        _64 = "#F75F3B",
        font_2 = "#776265",
        font_4 = "#776265"
    )
