from os import path
import unittest as ut
from wavefront_reader import read_objfile

class TestObjReader(ut.TestCase):
    def setUp(self):
        self.script_dir = path.dirname(__file__)

    def testGetVBOTriangles(self):
        obj_file = read_objfile(self.script_dir + "/wavefronts/cube.obj")
        cube = obj_file['Cube.002']
        first_four = [1.0, -1.0, 1.0, 1.0, 0.249684, 0.666956,
                      -1.0, -1.0, 1.0, 1.0, 0.000802, 0.666956,
                      -1.0, -1.0, -1.0, 1.0, 0.000802, 0.335112,
                      1.0, 1.0, -0.999999, 1.0, 0.498618, 0.668223]
        self.assertListEqual(cube.get_vbo_data_triangles()[:24], first_four)
        pass
