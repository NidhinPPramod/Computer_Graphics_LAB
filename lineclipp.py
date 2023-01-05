from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-50.0, 50.0, -50.0, 50.0)


def glutFunct():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Clipping Algorithms")
    init()
    
def drawClippingWindow(xWin0, xWinMax, yWin0, yWinMax):
    edges = [
        [0, 1],
        [1, 2],
        [2, 3],
        [3, 0]
    ]
    points = [
        [xWin0, yWin0],
        [xWinMax, yWin0],
        [xWinMax, yWinMax],
        [xWin0, yWinMax]
    ]
    rgb = (1.0, 1.0, 1.0)

    drawLines(edges, points, rgb)

def getClippingWindowSize():
    print("Enter the clipping window size : ")
    xWin0 = float(input("Enter the minimum window value of x : "))
    xWinMax = float(input("Enter the maximum window value of x : "))
    yWin0 = float(input("Enter the minimum window value of y : "))
    yWinMax = float(input("Enter the maximum window value of y : "))
    return xWin0, xWinMax, yWin0, yWinMax

def drawLines(edges, points, rgb):
    glColor3f(rgb[0], rgb[1], rgb[2])
    for e in edges:
        for v in e:
            glVertex2fv(points[v])

def getLine():
    x1 = float(input("Enter the initial x coordinate value : "))
    x2 = float(input('Enter the final x coordinate value : '))
    y1 = float(input("Enter the initial y coordinate value : "))
    y2 = float(input("Enter the final y coordinate value : "))

    return x1, x2, y1, y2


def drawGivenLine(x1, x2, y1, y2):
    edges = [
        [0, 1]
    ]
    points = [
        [x1, y1],
        [x2, y2]
    ]
    rgb = [0.0, 0.0, 1.0]

    drawLines(edges, points, rgb)


INSIDE = 0
LEFT = 1
RIGHT = 2
DOWN = 4
TOP = 8

def computeCode(x, y, xWin0, xWinMax, yWin0, yWinMax):
    code = INSIDE

    if x < xWin0:
        code |= LEFT

    elif x > xWinMax:
        code |= RIGHT

    if y < yWin0:
        code |= DOWN

    elif y > yWinMax:
        code |= TOP

    return code

def cohenSutherland(x1, x2, y1, y2, xWin0, xWinMax, yWin0, yWinMax):
    drawGivenLine(x1, x2, y1, y2)

    code1 = computeCode(x1, y1, xWin0, xWinMax, yWin0, yWinMax)
    code2 = computeCode(x2, y2, xWin0, xWinMax, yWin0, yWinMax)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break

        elif code1 & code2 != 0:
            break

        else:
            x = float()
            y = float()

            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            if code_out & TOP:
                y = yWinMax
                x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)

            elif code_out & DOWN:
                y = yWin0
                x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)

            elif code_out & LEFT:
                x = xWin0
                y = y1 + (x - x1) * (y2 - y1) / (x2 - x1)

            elif code_out & RIGHT:
                x = xWinMax
                y = y1 + (x - x1) * (y2 - y1) / (x2 - x1)

            if code_out == code1:
                x1, y1 = x, y
                code1 = computeCode(x, y, xWin0, xWinMax, yWin0, yWinMax)

            else:
                x2, y2 = x, y
                code2 = computeCode(x, y, xWin0, xWinMax, yWin0, yWinMax)

    if accept:
        edges = [[0, 1]]
        points = [
            [x1, y1],
            [x2, y2]
        ]
        rgb = [1.0, 0.0, 0.0]
        drawLines(edges, points, rgb)
        drawClippingWindow(xWin0, xWinMax, yWin0, yWinMax)

    else:
        print("The given line cannot be clipped!")


def clipLine(x1, x2, y1, y2, xWin0, xWinMax, yWin0, yWinMax):

    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(5.0)
    glBegin(GL_LINES)

    cohenSutherland(x1, x2, y1, y2, xWin0, xWinMax, yWin0, yWinMax)

    glEnd()
    glFlush()

def main():
        xWin0, xWinMax, yWin0, yWinMax = getClippingWindowSize()
        x1, x2, y1, y2 = getLine()
        glutFunct()
        glutDisplayFunc(lambda: clipLine(x1, x2, y1, y2, xWin0, xWinMax, yWin0, yWinMax))
        glutMainLoop()
main()
