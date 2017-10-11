import unittest as ut
from os import path
from wavefront_reader import read_mtlfile

class TestObjReader(ut.TestCase):
    def setUp(self):
        self.script_dir = path.dirname(__file__)

    def testFileExists(self):

        try:
            obj_file = open(self.script_dir + "/wavefronts/untitled.mtl")
            obj_file.close()
        except FileNotFoundError as fe:
            self.fail("Couldn't find file. " + str(fe))

    def test_all_materials_extracted(self):
        materials = read_mtlfile(self.script_dir + "/wavefronts/untitled.mtl")
        self.assertTrue(len(materials.material_list) == 1)

        materials = read_mtlfile(self.script_dir + "/wavefronts/two_complete_meshes.mtl")
        self.assertTrue(len(materials.material_list) == 2)

    def test_diffuse_values_correct(self):
        materials = read_mtlfile(self.script_dir + "/wavefronts/untitled.mtl")
        self.assertTrue(materials.last_material.Kd == (0.64, 0.64, 0.64))

    def test_illum(self):
        materials = read_mtlfile(self.script_dir + "/wavefronts/untitled.mtl")
        self.assertTrue(materials.last_material.illum == 2)
