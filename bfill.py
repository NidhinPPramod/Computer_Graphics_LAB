import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# for setting window size
window_size = 800
point_size = 5
sys.setrecursionlimit(100000)
boundary_fill_color = [1, 0, 0]


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


def plot_triangle():
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    gluOrtho2D(0, window_size, window_size, 0)
    glColor3f(1, 0, 0)
    glLineWidth(point_size)
    glBegin(GL_POLYGON)
    glVertex2f(200, 200)
    glVertex2f(400,200)
    glVertex2f(400,400)
    glEnd()
    glFlush()


def boundary_fill(x, y, fill_color, boundary_color):
    color = get_pixel(x, y)
    if (not all(color == fill_color)) and not all(color == boundary_color):

        set_pixel(x, y, fill_color)
        boundary_fill(x + point_size, y, fill_color, boundary_color)
        boundary_fill(x, y + point_size, fill_color, boundary_color)
        boundary_fill(x - point_size, y, fill_color, boundary_color)
        boundary_fill(x, y - point_size, fill_color, boundary_color)


def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        boundary_fill(x, y, [0, 0, 1], boundary_fill_color)


def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("Point")
    glutDisplayFunc(plot_triangle)
    glutMouseFunc(mouse_click)
    glutMainLoop()


if __name__ == '__main__':
    main()