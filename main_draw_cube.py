# From https:#stackoverflow.com/questions/16558819/vertex-buffer-objects-in-pyopengl-vertex-index-and-colour
# Search for: OpenGL Core Profile, VBO (Vertex buffer objects)

# C++ howto - gives some basic ideas
# http:#www.opengl-tutorial.org/beginners-tutorials/tutorial-2-the-first-triangle/

# Python example
# https:#gist.github.com/ousttrue/c4ae334fc1505cdf4cd7

from math import sqrt

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *

from figures.cube import Cube


class OpenGl():
    TRANSLATE_STEP = 2
    ROTATE_STEP = 2
    buffers = None

    I = len = g = m = None

    def __init__(self):
        self.sr2 = sqrt(0.75)

        # initialise GLUT and a few other things
        glutInit("")
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
        glutInitWindowSize(640, 480)
        glutInitWindowPosition(0, 0)

        self.rotate_x = -30
        self.rotate_y = 20
        self.rotate_z = 0
        self.translate_x = 0
        self.translate_y = 0
        self.translate_z = -50.0

        # create our window
        self.hWindow = glutCreateWindow("VBO testing")

        # setup the display function callback
        glutDisplayFunc(self.draw)

        # go full-screen if we want to
        # glutFullScreen()

        # setup the idle function callback -- if we idle, we just want to keep
        # drawing the screen
        glutIdleFunc(self.draw)
        # setup the window resize callback -- this is only needed if we arent going
        # full-screen
        glutReshapeFunc(self.on_resize)
        # setup the keyboard function callback to handle key presses
        glutKeyboardFunc(self.key_pressed)
        # Set the callback for special function
        glutSpecialFunc(self.special)

        # call our init function
        self.init_gl(640, 480)

        # enter the window's main loop to set things rolling
        glutMainLoop()

    def is_shift(self):
        return glutGetModifiers() == GLUT_ACTIVE_SHIFT

    def is_alt(self):
        return glutGetModifiers() == GLUT_ACTIVE_ALT

    def init_gl(self, nWidth, nHeight):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)

        self.cube = Cube()
        self.cube.add_solved_data()

        self.on_resize(nWidth, nHeight)

    def draw(self):
        """
        Draws
        the
        scene.
        :return:
        """

        # clear the screen and depth buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Resets the matrix stack with the identity matrix
        glLoadIdentity()

        # 'eyeX', 'eyeY', 'eyeZ', 'centerX', 'centerY', 'centerZ', 'upX', 'upY', 'upZ'
        # gluLookAt(0.0, 0.0, -100, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0)
        # glRotatef(-40, 0, 1, 0)

        glTranslatef(self.translate_x, self.translate_y, self.translate_z)

        glRotated(-self.rotate_x, 1, 0, 0)
        glRotated(-self.rotate_y, 0, 1, 0)
        glRotated(-self.rotate_z, 0, 0, 1)

        # self.default_piece.move_to((0, 0, 0))
        # self.default_piece.draw()

        self.cube.draw()

        # piece = list(self.cube)[0]
        # glPushMatrix()
        # piece.move_to((0, 0, 0))
        # # piece.move_to(piece.position)
        # piece.draw()
        # glPopMatrix()

        for piece in self.cube:
            glPushMatrix()
            piece.move_to(piece.position)
            piece.draw()
            glPopMatrix()

        # self.rotate_y -= self.ROTATE_STEP

        glDisableClientState(GL_COLOR_ARRAY)
        glDisableClientState(GL_VERTEX_ARRAY)

        # glBindBuffer(GL_ARRAY_BUFFER, self.buffers)
        # # glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0)
        # # Starting from vertex 0 3 vertices total -> 1 triangle
        # glDrawArrays(GL_TRIANGLES, 0, 3)
        # glDisableVertexAttribArray(0)

        glutSwapBuffers()

    rotational_factors = []
    initialized = None

    def on_resize(self, nWidth, nHeight):
        # prevent a divide-by-zero error if the window is too small
        if nHeight == 0:
            nHeight = 1

        # reset the current viewport and recalculate the perspective transformation
        # for the projection matrix
        glViewport(0, 0, nWidth, nHeight)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(nWidth) / float(nHeight), 0.1, 100.0)

        # return to the modelview matrix mode
        glMatrixMode(GL_MODELVIEW)

    def special(self, key, x, y):
        print(key)
        if self.is_alt():
            if key == GLUT_KEY_UP:
                self.translate_z += self.TRANSLATE_STEP
            elif key == GLUT_KEY_DOWN:
                self.translate_z -= self.TRANSLATE_STEP
            elif key == GLUT_KEY_LEFT:
                self.rotate_z -= self.ROTATE_STEP
            elif key == GLUT_KEY_RIGHT:
                self.rotate_z += self.ROTATE_STEP
        elif self.is_shift():
            if key == GLUT_KEY_UP:
                self.translate_y += self.TRANSLATE_STEP
            elif key == GLUT_KEY_DOWN:
                self.translate_y -= self.TRANSLATE_STEP
            elif key == GLUT_KEY_LEFT:
                self.translate_x -= self.TRANSLATE_STEP
            elif key == GLUT_KEY_RIGHT:
                self.translate_x += self.TRANSLATE_STEP
        else:
            if key == GLUT_KEY_UP:
                self.rotate_x += self.ROTATE_STEP
            elif key == GLUT_KEY_DOWN:
                self.rotate_x -= self.ROTATE_STEP
            elif key == GLUT_KEY_LEFT:
                self.rotate_y -= self.ROTATE_STEP
            elif key == GLUT_KEY_RIGHT:
                self.rotate_y += self.ROTATE_STEP

    def key_pressed(self, key, x, y):
        key = ord(key)
        print(key)
        if key == 27:
            glutDestroyWindow(self.hWindow)
            sys.exit()

        if key == KEY_R:
            print('Right')
            self.cube.R()
        elif key == KEY_Ri:
            print('Right inverted')
            self.cube.Ri()

        elif key == KEY_L:
            print('Left')
            self.cube.L()
        elif key == KEY_Li:
            print('Left inverted')
            self.cube.Li()

        elif key == KEY_F:
            print('Front')
            self.cube.F()
        elif key == KEY_Fi:
            print('Front inverted')
            self.cube.Fi()

        elif key == KEY_B:
            print('Back')
            self.cube.B()
        elif key == KEY_Bi:
            print('Back inverted')
            self.cube.Bi()

        elif key == KEY_U:
            print('Up')
            self.cube.U()
        elif key == KEY_Ui:
            print('Up inverted')
            self.cube.Ui()

        elif key == KEY_D:
            print('Down')
            self.cube.D()
        elif key == KEY_Di:
            print('Down inverted')
            self.cube.Di()


KEY_R = 114
KEY_Ri = 82
KEY_L = 108
KEY_Li = 76
KEY_F = 102
KEY_Fi = 70
KEY_B = 98
KEY_Bi = 66
KEY_U = 117
KEY_Ui = 85
KEY_D = 100
KEY_Di = 68

if __name__ == "__main__":
    print("Hit ESC key to quit.")
    opengl = OpenGl()
