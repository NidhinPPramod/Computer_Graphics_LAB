from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import sys

# for setting window size
window_size = 800
point_size = 10
sys.setrecursionlimit(100000)


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)


def get_pixel(x, y):
    pixel = glReadPixels(x, window_size - y, 1, 1, GL_RGB, GL_FLOAT)
    return np.array([round(x, 1) for x in pixel[0][0]])


def set_pixel(x, y, fill_color=(0, 0, 0)):
    glColor3f(*fill_color)
    glPointSize(point_size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def two_square():
    gluOrtho2D(0, window_size, window_size, 0)
    glColor3f(1.0,0.0,1.0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_POLYGON)
    glVertex2f(0,0)
    glVertex2f(400,0)
    glVertex2f(400,400)
    glVertex2f(0,400)
    glEnd()
    glFlush()


def flood_fill(x, y, new_color, old_color):
    color = get_pixel(x, y)
    if all(color == old_color):
        set_pixel(x, y, new_color)
        flood_fill(x + point_size, y, new_color, old_color)
        flood_fill(x, y + point_size, new_color, old_color)
        flood_fill(x - point_size, y, new_color, old_color)
        flood_fill(x, y - point_size, new_color, old_color)


def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        flood_fill(x, y, [0, 1, .5], get_pixel(x, y))


def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("Point")
    glutDisplayFunc(two_square)
    glutMouseFunc(mouse_click)
    glutMainLoop()


if __name__ == '__main__':
    main()