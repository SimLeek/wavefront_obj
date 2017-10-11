from os import path
import unittest as ut
from wavefront_reader import read_wavefront
from wavefront_reader.reading import Material


filepath = path.join(path.split(__file__)[0], '..', 'examples')

filenames = ['untitled.obj',
             'untitled_with_normals.obj',
             'untitled_with_normals_and_texcoords.obj',
             'two_complete_meshes.obj'
             ]

fnames = [path.join(filepath, name) for name in filenames]


class TestWavefrontReader(ut.TestCase):
    def setUp(self):
        self.script_dir = path.dirname(__file__)

    def test_all_materials_extracted(self):
        obj_1 = read_wavefront(self.script_dir + "/wavefronts/untitled.obj")
        obj_2 = read_wavefront(self.script_dir + "/wavefronts/two_complete_meshes.obj")
        self.assertTrue(len(obj_1.object_list) == 1)
        self.assertTrue(len(obj_2.object_list) == 2)

    def test_geoms_have_material_dict(self):
        obj_1 = read_wavefront(self.script_dir + "/wavefronts/untitled.obj")
        obj_2 = read_wavefront(self.script_dir + "/wavefronts/two_complete_meshes.obj")
        for geom in obj_1.object_list:
            self.assertTrue(geom.material_name != '')
            self.assertTrue(isinstance(geom.material, Material))
            self.assertTrue(geom.material.Kd is not None)
