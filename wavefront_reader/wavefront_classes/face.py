if False:
    from wavefront_reader.reading import Obj

class Face(object):
    def __init__(self,
                 parent_object  # type: Obj
                 ):
        self.vertex_indices = []
        self.vertex_texture_indices = []
        self.vertex_normal_indices = []
        self.parent_object = parent_object

    @property
    def vertices(self):
        return [self.parent_object.vertices[v - 1] for v in self.vertex_indices]

    @property
    def vertex_normals(self):
        return [self.parent_object.vertex_normals[v-1] for v in self.vertex_normal_indices]

    @property
    def vertex_textures(self):
        return [self.parent_object.vertex_textures[v-1] for v in self.vertex_texture_indices]
