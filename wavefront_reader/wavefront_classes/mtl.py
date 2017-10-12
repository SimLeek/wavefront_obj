if False:
    from typing import Tuple, Dict, Union
from collections import OrderedDict

class Mtl(object):
    def __init__(self, name):
        self.name = name
        self.Ns = None  # type: float
        self.Ka = None  # type: Tuple(float)
        self.Ke = None  # type: Tuple(float)
        self.Kd = None  # type: Tuple(float)
        self.Ks = None  # type: Tuple(float)
        self.Ni = None  # type: float
        self.d = None  # type: float
        self.illum = None  # type: int
        self.map_Kd = ''

        self.misc = OrderedDict()  # type: Dict[str, Union[float, Tuple[float]]]
