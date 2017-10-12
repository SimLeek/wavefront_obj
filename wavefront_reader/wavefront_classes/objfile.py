from wavefront_reader.wavefront_classes.obj import Obj
from wavefront_reader.wavefront_classes.face import Face

if False:
    from typing import Dict, List, Tuple
from collections import OrderedDict

class ObjFile(object):
    def __init__(self):
        self._obj_props = OrderedDict()  # type: Dict[str, Obj]
        self.last_obj_prop = None

        self.misc = OrderedDict()

    def __getitem__(self,
                    item  # type: str
                    ): # type: (...)->Obj
        return self.object_dict[item]

    def __setitem__(self,
                    key,  # type: str
                    value  # type: Obj
                    ):
        self.object_dict[key] = value

    @property
    def object_list(self):
        return [x[1] for x in self._obj_props.items()]

    @property
    def object_dict(self):
        return self._obj_props

    def add_prop(self, name):
        self._obj_props[name] = Obj(name)
        self.last_obj_prop = self.object_list[-1]

    def has_prop(self):
        return self.last_obj_prop is not None


    '''# todo: UNTESTED
    @classmethod
    def from_gl_triangles(cls,
                          name,
                          vao_array,  # type: List[float]
                          texture,
                          has_vertex_textures = True,
                          has_vertex_normals = False
                          ):
        obj_file = ObjFile()

        obj_file._obj_props[name] = Obj(name)

        vao_single_vertex_length = 4
        if has_vertex_normals:
            vao_single_vertex_length += 3
        if has_vertex_textures:
            vao_single_vertex_length += 2

        # convert glsl 4 dimensional verts to obj file 3 dimensional ones
        

        for v in range(len(vertices)):
            if (v%3 == 0):  # start new triangle
                obj_file[name].faces.append(Face(obj_file[name]))
            first_occurrance = vertices.index(vertices[v])
            if v!=first_occurrance:
                del(vertices[v])
            obj_file[name].faces[-1].vertex_indices.append(first_occurrance)

        obj_file[name].vertices = vertices

        pass'''
