from wavefront_reader.wavefront_classes.face import Face

def read_face(line, parent_obj):
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
