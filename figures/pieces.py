# noinspection PyUnresolvedReferences
from typing import Tuple, List

import numpy as np
from OpenGL.GL import *

from figures.helpers.color_indices import FRONT, DOWN, BACK, TOP, RIGHT, LEFT
from figures.square import Square


class BasePiece(object):
    cube: 'Cube' = None
    pos = (0, 0, 0)
    size = 4
    squares = None

    # x idx of the data structure numpy array
    x = None
    # y idx of the data structure numpy array
    y = None
    # z idx of the data structure numpy array
    z = None

    indices = [
        (0, 1, 2, 2, 3, 0),
        (0, 4, 7, 7, 3, 0),
        (4, 5, 6, 6, 7, 4),
        (1, 5, 6, 6, 2, 1),
        (3, 2, 6, 6, 7, 3),
        (0, 1, 5, 5, 4, 0),
    ]

    def __init__(self, cube: 'Cube', colors):
        self.cube = cube

        if not colors:
            raise Exception(f'No colors available for piece')

        if len(colors) != 6:
            raise Exception(f'Only {len(colors)} colors available for piece')

        self.colors = colors
        self.update_squares()

        self.create_buffers()

    def update_squares(self):
        self.squares = []
        for index, color in zip(self.indices, self.colors):
            self.squares.append(Square(size=self.size, indices=index, color=color))

    @property
    def position(self):
        return tuple(np.array(self.data_pos) * self.size)

    def set_data_position(self):
        res = np.where(self.cube.pieces == self)
        self.data_pos = (res[0][0], res[1][0], res[2][0])

    def move_to(self, pos: Tuple[float, float, float]):
        self.pos = pos
        glTranslatef(*self.pos)

    def move_rel(self, pos: Tuple[float, float, float]):
        self.pos = tuple(np.array(self.pos) + np.array(pos))
        glTranslatef(*self.pos)

    def create_buffers(self):
        for square in self.squares:
            square.create_buffers()

    def draw(self):
        for square in self.squares:
            square.draw()

    def flip_colors_x(self):
        colors_old = np.array(self.colors)
        self.colors[FRONT] = colors_old[DOWN]
        self.colors[DOWN] = colors_old[BACK]
        self.colors[BACK] = colors_old[TOP]
        self.colors[TOP] = colors_old[FRONT]
        self.update_squares()
        self.create_buffers()

    def flip_colors_xi(self):
        colors_old = np.array(self.colors)
        self.colors[FRONT] = colors_old[TOP]
        self.colors[TOP] = colors_old[BACK]
        self.colors[BACK] = colors_old[DOWN]
        self.colors[DOWN] = colors_old[FRONT]
        self.update_squares()
        self.create_buffers()

    def flip_colors_y(self):
        colors_old = np.array(self.colors)
        self.colors[FRONT] = colors_old[RIGHT]
        self.colors[RIGHT] = colors_old[BACK]
        self.colors[BACK] = colors_old[LEFT]
        self.colors[LEFT] = colors_old[FRONT]
        self.update_squares()
        self.create_buffers()

    def flip_colors_yi(self):
        colors_old = np.array(self.colors)
        self.colors[FRONT] = colors_old[LEFT]
        self.colors[LEFT] = colors_old[BACK]
        self.colors[BACK] = colors_old[RIGHT]
        self.colors[RIGHT] = colors_old[FRONT]
        self.update_squares()
        self.create_buffers()

    def flip_colors_z(self):
        colors_old = np.array(self.colors)
        self.colors[TOP] = colors_old[LEFT]
        self.colors[LEFT] = colors_old[DOWN]
        self.colors[DOWN] = colors_old[RIGHT]
        self.colors[RIGHT] = colors_old[TOP]
        self.update_squares()
        self.create_buffers()

    def flip_colors_zi(self):
        colors_old = np.array(self.colors)
        self.colors[TOP] = colors_old[RIGHT]
        self.colors[RIGHT] = colors_old[DOWN]
        self.colors[DOWN] = colors_old[LEFT]
        self.colors[LEFT] = colors_old[TOP]
        self.update_squares()
        self.create_buffers()


# Totally 1 piece in the middle of the cube
# No color
class Piece(BasePiece):
    def __init__(self, *args, **kwargs):
        super(Piece, self).__init__(*args, **kwargs, colors=[None, None, None, None, None, None])

    def __str__(self):
        return ' - '


# Totally 6
# Piece with one color
class MiddlePiece(BasePiece):
    def __init__(self, *args, **kwargs):
        super(MiddlePiece, self).__init__(*args, **kwargs)


# Totally 12
# Piece with 2 colors
class EdgePiece(BasePiece):
    def __init__(self, *args, **kwargs):
        super(EdgePiece, self).__init__(*args, **kwargs)


# Totally 8
# Piece with 3 colors
class CornerPiece(BasePiece):
    def __init__(self, *args, **kwargs):
        super(CornerPiece, self).__init__(*args, **kwargs)
