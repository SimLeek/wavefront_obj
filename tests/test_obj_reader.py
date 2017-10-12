#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
import unittest as ut
from wavefront_reader import read_objfile


class TestObjReader(ut.TestCase):
    def setUp(self):
        self.script_dir = path.dirname(__file__)

    def testFileExists(self):

        try:
            obj_file = open(self.script_dir + "/wavefronts/untitled.obj")
            obj_file.close()
        except FileNotFoundError as fe:
            self.fail("Couldn't find file. " + str(fe))

    def testHasVertices(self):
        obj_file = read_objfile(self.script_dir + "/wavefronts/untitled.obj")
        cube = obj_file['Cube']
        self.assertTrue(len(cube.vertices) > 0)

    def test_has_normals(self):
        geoms = read_objfile(self.script_dir + "/wavefronts/untitled_with_normals.obj")
        cube = geoms['Cube']
        self.assertTrue(len(cube.vertex_normals) > 0)

    def test_has_no_normals(self):
        geoms = read_objfile(self.script_dir + "/wavefronts/untitled.obj")
        cube = geoms['Cube']
        self.assertTrue(len(cube.vertex_normals) == 0)

    def test_has_texcoords(self):
        geoms = read_objfile(self.script_dir + "/wavefronts/untitled_with_normals_and_texcoords.obj")
        cube = geoms['Cube']
        self.assertTrue(len(cube.vertex_textures) > 0)

    def test_has_no_texcoords(self):
        geoms = read_objfile(self.script_dir + "/wavefronts/untitled_with_normals.obj")
        cube = geoms['Cube']
        self.assertTrue(len(cube.vertex_textures) == 0)

    def test_has_n_meshes(self):
        geoms = read_objfile(self.script_dir + "/wavefronts/untitled_with_normals.obj")
        self.assertTrue(len(geoms.object_list) == 1)
        geoms = read_objfile(self.script_dir + "/wavefronts/two_complete_meshes.obj")
        self.assertTrue(len(geoms.object_list) == 2)
