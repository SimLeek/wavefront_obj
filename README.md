# wavefront_reader

A parser for wavefront .obj and .mtl files

* Free software: MIT license
* Documentation: TBD


Features
--------

Reads out wavefront objects to dictionaries with their attributes, including their materials:

    from wavefront_reader import read_wavefront, read_objfile, read_mtlfile
    geoms = read_wavefront('myObjects.obj')
    cube = geoms['Cube']
    cube_vertices = cube.vertexes
    cube_diffuse_material = cube['material']['Kd']

The module has a lot of tests, and handles face indexing by re-indexing the vertex, normal, and texcoord arrays
simply by reindexing them into same-length, sequential arrays.  While this reduces the memory benefits of the .obj
format, it makes it much easier to load the data into OpenGL or reindex the data yourself.

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

