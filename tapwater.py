from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy
import math
import sys

sys.setrecursionlimit(10**8)

window=500
ty=0
r=200
yfill=-195
theta1=265
theta2=275


def init():
    glClear(GL_COLOR_BUFFER_BIT)
    gluOrtho2D(-window,window,-window,window)

def circle():
    i=3.14
    xc=0
    yc=0
    glColor3f(1, 0, 0)
    glBegin(GL_POINTS)
    while i<6.28:
        glVertex2f(r*math.cos(i)+xc,r*math.sin(i)+yc)
        i+=.01
    glEnd()


def tap():
    glColor3f(0, 1, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-100,window)
    glVertex2f(100,window)
    glVertex2f(100,window-150)
    glVertex2f(-100,window-150)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-15,window-250+ty)
    glVertex2f(15,window-250+ty)
    glVertex2f(15,window-260+ty)
    glVertex2f(-15,window-260+ty)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-15,window-270+ty)
    glVertex2f(15,window-270+ty)
    glVertex2f(15,window-280+ty)
    glVertex2f(-15,window-280+ty)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-15,window-285+ty)
    glVertex2f(15,window-285+ty)
    glVertex2f(15,window-295+ty)
    glVertex2f(-15,window-295+ty)
    glEnd()


def filling():
    global theta1,theta2,yfill
    glBegin(GL_LINES)
    for i in range(theta1,theta2,1):
        glVertex2f(0,yfill)
        glVertex2f(198*math.cos(math.radians(i)), 198*math.sin(math.radians(i)))
    glEnd()


def draw():  
    glClear(GL_COLOR_BUFFER_BIT)
    circle()
    tap()
    filling()
    glFlush()
    glutSwapBuffers()

def animate(temp):
    global ty,yfill,theta1,theta2
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))

    if(ty==-400):
        ty=0
        yfill=yfill+10
        theta1-=5
        theta2+=5
    
    if(theta1==180 and theta2==360):
        theta1=265
        theta2=275
        yfill=-195

    ty-=4



def main():
    glutInit()
    glutInitWindowPosition(50,50)
    glutInitWindowSize(window,window)
    glutCreateWindow("Tap Water")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    init()
    glutMainLoop()

main()