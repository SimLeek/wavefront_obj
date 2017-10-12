from wavefront_reader.wavefront_classes.objfile import ObjFile
from .readface import read_face

def read_objfile(fname):
    """Takes .obj filename and return an ObjFile class."""
    obj_file = ObjFile()

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
                    obj_file.last_obj_prop.vertices.append([float(val) for val in value.split(' ')])
                elif prefix == 'vn':
                    obj_file.last_obj_prop.vertex_normals.append([float(val) for val in value.split(' ')])
                elif prefix == 'vt':
                    obj_file.last_obj_prop.vertex_textures.append([float(val) for val in value.split(' ')])
                elif prefix == 'usemtl':
                    obj_file.last_obj_prop.material_name = value
                elif prefix == 'f':
                    obj_file.last_obj_prop.faces.append(read_face(value, obj_file.last_obj_prop))
                else:
                    obj_file.misc[prefix] = value

    return obj_file
