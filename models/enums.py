from enum import Enum

class WxStarModel(str, Enum):
    i2jr = "i2jr"
    i2xd = "i2xd"
    i2hd = "i2hd"
    i2_generic = "i2"
    i1_generic = "i1"
    wsxl = "wsxl"
    custom = "custom"