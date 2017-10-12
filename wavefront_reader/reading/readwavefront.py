from .readobjfile import read_objfile
from .readmtlfile import read_mtlfile

from os import path

def read_wavefront(fname_obj):
    """Returns mesh class along with their material class from a wavefront (.obj and/or .mtl) file."""
    obj_file = read_objfile(fname_obj)

    # todo: this assumes only one material library per object file
    fname_mtl = ''
    for line in open(fname_obj):
        if line.strip():
            prefix, data = line.strip().split(' ', 1)
            if 'mtllib' in prefix:
                fname_mtl = data
                break

    if fname_mtl:
        mat_file = read_mtlfile(path.join(path.dirname(fname_obj), fname_mtl))

        for obj in obj_file.object_list:
            obj.material = mat_file.materials[obj.material_name]

    return obj_file
