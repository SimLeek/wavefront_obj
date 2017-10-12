raise NotImplementedError

from wavefront_reader import __version__ as wavefront_reader_version
from sys import version as python_version

from wavefront_reader.reading.readobjfile import ObjFile

class Writer(object):

    def __init__(self,
                 objfile = ObjFile()
                 ):
        self.preamble = "# Python{} wavefront_reader v{}: \n'".format(python_version, wavefront_reader_version)
        self.objfile = objfile

