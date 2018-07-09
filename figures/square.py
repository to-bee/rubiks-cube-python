# noinspection PyUnresolvedReferences
import math
from typing import Tuple

from OpenGL.GL import *
from OpenGL.GLUT import *

from figures.helpers.colors import GRAY


class Square(object):
    default_color = GRAY

    def __init__(self, size: int, indices: Tuple, color):
        super(Square, self).__init__()

        size = size / 2
        self.vertices = [
            -size, -size, size,  # 0, ldf
            size, -size, size,  # 1 rdf
            size, size, size,  # 2 rtf
            -size, size, size,  # 3 ltf
            -size, -size, -size,  # 4 ldb
            size, -size, -size,  # 5 rdb
            size, size, -size,  # 6 rtb
            -size, size, -size  # 7 ltb
        ]

        if color is None:
            color = Square.default_color

        self.colors = (
            *color,
            *color,
            *color,
            *color,
            *color,
            *color,
            *color,
            *color,
        )
        self.indices = indices

    vertices = []
    indices = []
    colors = []

    def create_buffers(self):
        self.buffers = glGenBuffers(3)
        glBindBuffer(GL_ARRAY_BUFFER, self.buffers[0])
        glBufferData(GL_ARRAY_BUFFER,
                     len(self.vertices) * 4,  # byte size
                     (ctypes.c_float * len(self.vertices))(*self.vertices),
                     GL_STATIC_DRAW)
        glBindBuffer(GL_ARRAY_BUFFER, self.buffers[1])
        glBufferData(GL_ARRAY_BUFFER,
                     len(self.colors) * 4,  # byte size
                     (ctypes.c_float * len(self.colors))(*self.colors),
                     GL_STATIC_DRAW)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.buffers[2])
        glBufferData(GL_ELEMENT_ARRAY_BUFFER,
                     len(self.indices) * 4,  # byte size
                     (ctypes.c_uint * len(self.indices))(*self.indices),
                     GL_STATIC_DRAW)

    def draw(self):
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)
        glBindBuffer(GL_ARRAY_BUFFER, self.buffers[0])

        glVertexPointer(3, GL_FLOAT, 0, None)
        glBindBuffer(GL_ARRAY_BUFFER, self.buffers[1])
        glColorPointer(3, GL_FLOAT, 0, None)

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.buffers[2])
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)

    def rotate_x(self):
        glPushMatrix()
        glRotated(20, 1, 0, 0)
        self.draw()
        glPopMatrix()
