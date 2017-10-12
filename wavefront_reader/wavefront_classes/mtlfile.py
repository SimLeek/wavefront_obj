from .mtl import Mtl
if False:
    from typing import Dict
from collections import OrderedDict


class MtlFile(object):
    def __init__(self):
        self.materials = OrderedDict()  # type: Dict[str, Mtl]

    @property
    def material_list(self):
        return [x[1] for x in self.materials.items()]

    @property
    def material_dict(self):
        return self.materials

    @property
    def last_material(self):
        return self.material_list[-1] if len(self.material_list)>0 else None

    def has_materials(self):
        return self.last_material is not None


    def add_material(self, name):
        self.materials[name] = Mtl(name)
