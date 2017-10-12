from wavefront_reader.wavefront_classes import MtlFile

def read_mtlfile(fname):
    mat_file = MtlFile()

    with open(fname) as f:
        lines = f.read().splitlines()

    for line in lines:
        if line:
            prefix, data = line.split(' ', 1)
            if 'newmtl' in prefix:
                mat_file.add_material(data)
            elif mat_file.has_materials():
                if prefix == 'Ns':
                    mat_file.last_material.Ns = float(data)
                elif prefix == 'Ka':
                    mat_file.last_material.Ka = tuple(float(d) for d in data.split(' '))
                elif prefix == 'Kd':
                    mat_file.last_material.Kd = tuple(float(d) for d in data.split(' '))
                elif prefix == 'Ks':
                    mat_file.last_material.Ks = tuple(float(d) for d in data.split(' '))
                elif prefix == 'Ke':
                    mat_file.last_material.Ke = tuple(float(d) for d in data.split(' '))
                elif prefix == 'Ni':
                    mat_file.last_material.Ni = float(data)
                elif prefix == 'd':
                    mat_file.last_material.d = float(data)
                elif prefix == 'illum':
                    mat_file.last_material.illum = int(data)
                elif prefix == 'map_Kd':
                    mat_file.last_material.map_Kd = data
                else:
                    try:
                        mat_file.last_material.misc[prefix] = int(data)
                    except ValueError:
                        mat_file.last_material.misc[prefix] = float(data)

    return mat_file
