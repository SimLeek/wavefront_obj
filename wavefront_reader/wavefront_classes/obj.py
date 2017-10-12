from wavefront_reader.wavefront_classes.face import Face
if False:
    from typing import List
    from wavefront_reader.wavefront_classes import Mtl

class Obj(object):
    def __init__(self, name  # type: str
                 ):
        self.name = name
        self.obj_props = []
        self.vertices = []
        self.vertex_normals = []
        self.vertex_textures = []
        self.faces = []  # type: List[Face]
        self._current_obj_prop = None
        self.material_name = ''
        self.material = None  # type: Mtl

        self.misc = []

    def add_prop(self, prefix, value):
        self.obj_props.append({})
        self._current_obj_prop = self.obj_props[-1]
        self._current_obj_prop['f'] = []
        self._current_obj_prop[prefix] = value

    def has_prop(self):
        return self._current_obj_prop is not None

    def has_vertex_normals(self):
        return len(self.vertex_normals) > 0

    def has_vertex_textures(self):
        return len(self.vertex_textures) > 0

    def get_vao_data_triangles(self):
        gl_array = []

        single_gl_vertex_len = 4
        if self.has_vertex_textures():
            single_gl_vertex_len += 2
        if self.has_vertex_normals():
            #single_gl_vertex_len += 3
            #ignore for now
            pass

        for face in self.faces:
            for fv in range(len(face.vertices)):
                if (fv >= 3):
                    raise TypeError("Not a triangle mesh")
                if (len(face.vertices[fv]) != 3):
                    raise TypeError("incorrect vertex length")
                gl_array.extend(face.vertices[fv])
                gl_array.append(1.0)  # add the extra point for translation and stuff

                if self.has_vertex_normals():
                    pass
                #    if (len(face.vertex_normals[fv]) != 3):
                #        raise TypeError("incorrect vertex_normal length")
                #    gl_array.append(*face.vertex_normals[fv])

                if self.has_vertex_textures():
                    if (len(face.vertex_textures[fv]) != 2):
                        raise TypeError("incorrect vertex_texture length")
                    gl_array.extend(face.vertex_textures[fv])




        return gl_array
