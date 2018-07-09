# noinspection PyUnresolvedReferences
import numpy as np

from figures.helpers.colors import ORANGE, RED, GREEN, BLUE, WHITE, YELLOW
from figures.helpers.cube_indexes import right_rotation_top, right_rotation_front, right_rotation_down, right_rotation_back, left_rotation_top, left_rotation_front, left_rotation_back, left_rotation_down, front_rotation_top, front_rotation_right, front_rotation_down, front_rotation_left, back_rotation_top, back_rotation_right, back_rotation_down, back_rotation_left, up_rotation_left, up_rotation_front, up_rotation_right, up_rotation_back, down_rotation_left, down_rotation_back, down_rotation_right, down_rotation_front, right, left, front, back, up, down
from figures.pieces import Piece, CornerPiece, EdgePiece, MiddlePiece


class Cube(object):
    """
    Totally 3x3x3 = 27 pieces
    """
    num_pieces = 3
    pieces = np.full((num_pieces, num_pieces, num_pieces), None, dtype=Piece)  # x,y,z

    def __init__(self):
        pass

    def flip_colors_x(self, pieces):
        for piece in self.pieces[pieces].flat:
            piece.flip_colors_x()

    def flip_colors_xi(self, slice):
        for piece in self.pieces[slice].flat:
            piece.flip_colors_xi()

    def flip_colors_y(self, slice):
        for piece in self.pieces[slice].flat:
            piece.flip_colors_y()

    def flip_colors_yi(self, slice):
        for piece in self.pieces[slice].flat:
            piece.flip_colors_yi()

    def flip_colors_z(self, slice):
        for piece in self.pieces[slice].flat:
            piece.flip_colors_z()

    def flip_colors_zi(self, slice):
        for piece in self.pieces[slice].flat:
            piece.flip_colors_zi()

    def R(self):
        pieces_old = np.array(self.pieces)
        self.pieces[right_rotation_top()] = np.flip(pieces_old[right_rotation_front()], axis=0)
        self.pieces[right_rotation_front()] = pieces_old[right_rotation_down()]
        self.pieces[right_rotation_down()] = np.flip(pieces_old[right_rotation_back()], axis=0)
        self.pieces[right_rotation_back()] = pieces_old[right_rotation_top()]

        self.flip_colors_x(right())
        self.update_data_positions()

    def Ri(self):
        pieces_old = np.array(self.pieces)
        self.pieces[right_rotation_top()] = pieces_old[right_rotation_back()]
        self.pieces[right_rotation_back()] = np.flip(pieces_old[right_rotation_down()], axis=0)
        self.pieces[right_rotation_down()] = pieces_old[right_rotation_front()]
        self.pieces[right_rotation_front()] = np.flip(pieces_old[right_rotation_top()], axis=0)

        self.flip_colors_xi(right())
        self.update_data_positions()

    def L(self):
        pieces_old = np.array(self.pieces)
        self.pieces[left_rotation_front()] = np.flip(pieces_old[left_rotation_top()], axis=0)
        self.pieces[left_rotation_top()] = pieces_old[left_rotation_back()]
        self.pieces[left_rotation_back()] = np.flip(pieces_old[left_rotation_down()], axis=0)
        self.pieces[left_rotation_down()] = pieces_old[left_rotation_front()]

        self.flip_colors_xi(left())
        self.update_data_positions()

    def Li(self):
        pieces_old = np.array(self.pieces)
        self.pieces[left_rotation_front()] = pieces_old[left_rotation_down()]
        self.pieces[left_rotation_down()] = np.flip(pieces_old[left_rotation_back()], axis=0)
        self.pieces[left_rotation_back()] = pieces_old[left_rotation_top()]
        self.pieces[left_rotation_top()] = np.flip(pieces_old[left_rotation_front()], axis=0)

        self.flip_colors_x(left())
        self.update_data_positions()

    def F(self):
        pieces_old = np.array(self.pieces)
        self.pieces[front_rotation_top()] = pieces_old[front_rotation_left()]
        self.pieces[front_rotation_left()] = np.flip(pieces_old[front_rotation_down()], axis=0)
        self.pieces[front_rotation_down()] = pieces_old[front_rotation_right()]
        self.pieces[front_rotation_right()] = np.flip(pieces_old[front_rotation_top()], axis=0)

        self.update_data_positions()
        self.flip_colors_z(front())

    def Fi(self):
        pieces_old = np.array(self.pieces)
        self.pieces[front_rotation_top()] = np.flip(pieces_old[front_rotation_right()], axis=0)
        self.pieces[front_rotation_right()] = pieces_old[front_rotation_down()]
        self.pieces[front_rotation_down()] = np.flip(pieces_old[front_rotation_left()], axis=0)
        self.pieces[front_rotation_left()] = pieces_old[front_rotation_top()]

        self.update_data_positions()
        self.flip_colors_zi(front())

    def B(self):
        pieces_old = np.array(self.pieces)
        self.pieces[back_rotation_top()] = np.flip(pieces_old[back_rotation_right()], axis=0)
        self.pieces[back_rotation_right()] = pieces_old[back_rotation_down()]
        self.pieces[back_rotation_down()] = np.flip(pieces_old[back_rotation_left()], axis=0)
        self.pieces[back_rotation_left()] = pieces_old[back_rotation_top()]

        self.update_data_positions()
        self.flip_colors_zi(back())

    def Bi(self):
        pieces_old = np.array(self.pieces)
        self.pieces[back_rotation_top()] = pieces_old[back_rotation_left()]
        self.pieces[back_rotation_left()] = np.flip(pieces_old[back_rotation_down()], axis=0)
        self.pieces[back_rotation_down()] = pieces_old[back_rotation_right()]
        self.pieces[back_rotation_right()] = np.flip(pieces_old[back_rotation_top()], axis=0)

        self.update_data_positions()
        self.flip_colors_z(back())

    def U(self):
        pieces_old = np.array(self.pieces)
        self.pieces[up_rotation_left()] = pieces_old[up_rotation_front()]
        self.pieces[up_rotation_front()] = np.flip(pieces_old[up_rotation_right()], axis=0)
        self.pieces[up_rotation_right()] = pieces_old[up_rotation_back()]
        self.pieces[up_rotation_back()] = np.flip(pieces_old[up_rotation_left()], axis=0)

        self.update_data_positions()
        self.flip_colors_y(up())

    def Ui(self):
        pieces_old = np.array(self.pieces)
        self.pieces[up_rotation_left()] = np.flip(pieces_old[up_rotation_back()], axis=0)
        self.pieces[up_rotation_back()] = pieces_old[up_rotation_right()]
        self.pieces[up_rotation_right()] = np.flip(pieces_old[up_rotation_front()], axis=0)
        self.pieces[up_rotation_front()] = pieces_old[up_rotation_left()]

        self.update_data_positions()
        self.flip_colors_yi(up())

    def D(self):
        pieces_old = np.array(self.pieces)
        self.pieces[down_rotation_left()] = np.flip(pieces_old[down_rotation_back()], axis=0)
        self.pieces[down_rotation_back()] = pieces_old[down_rotation_right()]
        self.pieces[down_rotation_right()] = np.flip(pieces_old[down_rotation_front()], axis=0)
        self.pieces[down_rotation_front()] = pieces_old[down_rotation_left()]

        self.update_data_positions()
        self.flip_colors_yi(down())

    def Di(self):
        pieces_old = np.array(self.pieces)
        self.pieces[down_rotation_left()] = pieces_old[down_rotation_front()]
        self.pieces[down_rotation_front()] = np.flip(pieces_old[down_rotation_right()], axis=0)
        self.pieces[down_rotation_right()] = pieces_old[down_rotation_back()]
        self.pieces[down_rotation_back()] = np.flip(pieces_old[down_rotation_left()], axis=0)

        self.update_data_positions()
        self.flip_colors_y(down())

    def S(self):
        # TODO
        pass

    def Si(self):
        # TODO
        pass

    def X(self):
        # TODO
        pass

    def Xi(self):
        # TODO
        pass

    def Y(self):
        # TODO
        pass

    def Yi(self):
        # TODO
        pass

    def add_solved_data(self):
        # Front
        y = 0
        z = 2

        self.pieces[0, y, z] = CornerPiece(cube=self, colors=[ORANGE, GREEN, None, None, YELLOW, WHITE])
        self.pieces[1, y, z] = EdgePiece(cube=self, colors=[ORANGE, None, None, None, YELLOW, WHITE])
        self.pieces[2, y, z] = CornerPiece(cube=self, colors=[ORANGE, None, None, BLUE, YELLOW, WHITE])

        y += 1

        self.pieces[0, y, z] = EdgePiece(cube=self, colors=[ORANGE, GREEN, None, None, None, None])
        self.pieces[1, y, z] = MiddlePiece(cube=self, colors=[ORANGE, None, None, None, None, None])
        self.pieces[2, y, z] = EdgePiece(cube=self, colors=[ORANGE, None, None, BLUE, None, None])

        y += 1

        self.pieces[0, y, z] = CornerPiece(cube=self, colors=[ORANGE, GREEN, None, None, YELLOW, None])
        self.pieces[1, y, z] = EdgePiece(cube=self, colors=[ORANGE, None, None, None, YELLOW, None])
        self.pieces[2, y, z] = CornerPiece(cube=self, colors=[ORANGE, None, None, BLUE, YELLOW, None])

        # Middle
        y = 0
        z = 1

        self.pieces[0, y, z] = EdgePiece(cube=self, colors=[None, GREEN, None, None, None, WHITE])
        self.pieces[1, y, z] = MiddlePiece(cube=self, colors=[None, None, None, None, None, WHITE])
        self.pieces[2, y, z] = EdgePiece(cube=self, colors=[None, None, None, BLUE, None, WHITE])

        y += 1

        self.pieces[0, y, z] = MiddlePiece(cube=self, colors=[None, GREEN, None, None, None, None])
        self.pieces[1, y, z] = Piece(cube=self)
        self.pieces[2, y, z] = MiddlePiece(cube=self, colors=[None, None, None, BLUE, None, None])

        y += 1

        self.pieces[0, y, z] = EdgePiece(cube=self, colors=[None, GREEN, None, None, YELLOW, None])
        self.pieces[1, y, z] = MiddlePiece(cube=self, colors=[None, None, None, None, YELLOW, None])
        self.pieces[2, y, z] = EdgePiece(cube=self, colors=[None, None, None, BLUE, YELLOW, None])

        # Back
        y = 0
        z = 0
        self.pieces[0, y, z] = CornerPiece(cube=self, colors=[None, GREEN, RED, None, None, WHITE])
        self.pieces[1, y, z] = EdgePiece(cube=self, colors=[None, None, RED, None, None, WHITE])
        self.pieces[2, y, z] = CornerPiece(cube=self, colors=[None, None, RED, BLUE, None, WHITE])

        y += 1

        self.pieces[0, y, z] = EdgePiece(cube=self, colors=[None, GREEN, RED, None, None, None])
        self.pieces[1, y, z] = MiddlePiece(cube=self, colors=[None, None, RED, None, None, None])
        self.pieces[2, y, z] = EdgePiece(cube=self, colors=[None, None, RED, BLUE, None, None])

        y += 1

        self.pieces[0, y, z] = CornerPiece(cube=self, colors=[None, GREEN, RED, None, YELLOW, None])
        self.pieces[1, y, z] = EdgePiece(cube=self, colors=[None, None, RED, None, YELLOW, None])
        self.pieces[2, y, z] = CornerPiece(cube=self, colors=[None, None, RED, BLUE, YELLOW, None])

        self.update_data_positions()

    def __iter__(self):
        return iter(list(np.array(self.pieces).reshape(-1, )))

    def __str__(self):
        values = []
        for z, label in zip(range(self.pieces.shape[2]), ['Front', 'Middle', 'Back']):
            values.append(f'{label}')

            for y in range(self.pieces.shape[1]):
                values.append(' '.join([self.pieces[x, y, z].__str__() for x in range(self.pieces.shape[0])]))

        return '\n'.join(values)

    def draw(self):
        pass

    def update_data_positions(self):
        for piece in self:
            piece.set_data_position()
