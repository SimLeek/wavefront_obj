# -*- coding: utf-8 -*-
import numpy as np
from collections import namedtuple, OrderedDict
from six import iteritems
from os import path

if False:
    from typing import List, Dict

class Face(object):
    def __init__(self,
                 parent_object  # type: ObjectFile
                 ):
        self.vertex_indices = []
        self.vertex_texture_indices = []
        self.vertex_normal_indices = []
        self.parent_object = parent_object

    @property
    def vertexes(self):
        return [self.parent_object.vertexes[v] for v in self.vertex_indices]

    @property
    def vertex_normals(self):
        return [self.parent_object.vertex_normals[v] for v in self.vertex_normal_indices]

    @property
    def vertex_textures(self):
        return [self.parent_object.vertex_textures[v] for v in self.vertex_texture_indices]

def parse_mixed_delim_str(line, parent_obj):
    """Turns .obj face index string line into [verts, texcoords, normals] numeric tuples."""
    face = Face(parent_obj)
    arrs = [[], [], []]
    for group in line.split(' '):
        for type, coord in enumerate(group.split('/')):
            if type == 0 and coord:
                face.vertex_indices.append(int(coord))
            elif type == 1 and coord:
                face.vertex_texture_indices.append(int(coord))
            elif type == 2 and coord:
                face.vertex_normal_indices.append(int(coord))

    return face

class Object(object):
    def __init__(self, name  # type: str
                 ):
        self.name = name
        self.obj_props = []
        self.vertexes = []
        self.vertex_normals = []
        self.vertex_textures = []
        self.faces = []  # type: List[Face]
        self._current_obj_prop = None

        self.misc = []

    def add_prop(self, prefix, value):
        self.obj_props.append({})
        self._current_obj_prop = self.obj_props[-1]
        self._current_obj_prop['f'] = []
        self._current_obj_prop[prefix] = value

    def has_prop(self):
        return self._current_obj_prop is not None


class ObjectFile(object):
    def __init__(self):
        self._obj_props = OrderedDict()  # type: Dict[str, Object]
        self.last_obj_prop = None

        self.misc = OrderedDict()

    def __getitem__(self,
                    item  # type: str
                    ): # type: (...)->Object
        return self.object_dict[item]

    def __setitem__(self,
                    key,  # type: str
                    value  # type: Object
                    ):
        self.object_dict[key] = value

    @property
    def object_list(self):
        return [x[1] for x in self._obj_props.items()]

    @property
    def object_dict(self):
        return self._obj_props

    def add_prop(self, name):
        self._obj_props[name] = Object(name)
        self.last_obj_prop = self.object_list[-1]

    def has_prop(self):
        return self.last_obj_prop is not None


def read_objfile(fname):
    """Takes .obj filename and return an ObjectFile class."""
    obj_file = ObjectFile()

    with open(fname) as f:
        lines = f.read().splitlines()

    if 'OBJ' not in lines[0]:
        raise ValueError("File not .obj-formatted.")

    # todo: assumes one object per .obj file, which is wrong
    # todo: doesn't properly ignore comments
    for line in lines:
        if line:
            prefix, value = line.split(' ', 1)
            if prefix == 'o':
                obj_file.add_prop(value)
            if obj_file.has_prop():
                if prefix == 'v':
                    obj_file.last_obj_prop.vertexes.append([float(val) for val in value.split(' ')])
                elif prefix == 'vn':
                    obj_file.last_obj_prop.vertex_normals.append([float(val) for val in value.split(' ')])
                elif prefix == 'vt':
                    obj_file.last_obj_prop.vertex_textures.append([float(val) for val in value.split(' ')])
                elif prefix == 'f':
                    obj_file.last_obj_prop.faces.append(parse_mixed_delim_str(value, obj_file.last_obj_prop))
                else:
                    obj_file.misc[prefix] = value

    return obj_file

class MaterialFile(object):
    def __init__(self):
        pass

def read_mtlfile(fname):
    materials = {}
    with open(fname) as f:
        lines = f.read().splitlines()

    for line in lines:
        if line:
            prefix, data = line.split(' ', 1)
            if 'newmtl' in prefix:
                material = {}
                materials[data] = material
            elif materials:
                if len(data.split(' ')) > 1:
                    material[prefix] = tuple(float(d) for d in data.split(' '))
                else:
                    try:
                        material[prefix] = int(data)
                    except ValueError:
                        material[prefix] = float(data)

    return materials


def read_wavefront(fname_obj):
    """Returns mesh dictionary along with their material dictionary from a wavefront (.obj and/or .mtl) file."""
    fname_mtl = ''
    geoms = read_objfile(fname_obj)
    for line in open(fname_obj):
        if line.strip():
            prefix, data = line.strip().split(' ', 1)
            if 'mtllib' in prefix:
                fname_mtl = data
                break

    if fname_mtl:
        materials = read_mtlfile(path.join(path.dirname(fname_obj), fname_mtl))

        for geom in geoms.values():
            geom['material'] = materials[geom['usemtl']]

    return geoms


