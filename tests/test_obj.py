from os import path
import unittest as ut
from wavefront_reader import read_objfile

class TestObjReader(ut.TestCase):
    def setUp(self):
        self.script_dir = path.dirname(__file__)

    def testGetVAOTriangles(self):
        obj_file = read_objfile(self.script_dir + "/wavefronts/cube.obj")
        cube = obj_file['Cube.002']
        print(cube.get_vao_data_triangles())
