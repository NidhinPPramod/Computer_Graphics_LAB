from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

window=500
DIR=0
theta=0
tx=0

def init_disp():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(2)
    gluOrtho2D(-window,window,-window,window)

def boat():
    theta=0
    xc=0
    yc=70
    r=10
    i=0
    glColor3f(0.2,0.1,0.4)
    glBegin(GL_POLYGON)
    glVertex2f(150+tx, 0)
    glVertex2f(-150+tx, 0)
    glVertex2f(-100+tx,-50)
    glVertex2f(100+tx, -50)
    glEnd()
    glColor3f(.8,.6,0.5)
    glBegin(GL_POLYGON)
    glVertex2f(10+tx, 0)
    glVertex2f(-10+tx, 0)
    glVertex2f(-10+tx,50)
    glVertex2f(10+tx, 50)
    glEnd()
    glBegin(GL_LINES)
    while i <6.28:
        glVertex2f(xc+tx, yc)
        glVertex2f(r*math.cos(i)+xc+tx, r*math.sin(i)+yc)
        i+=.01
    glEnd()

def row():
    glColor3f(1.0,1.0,1.0)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(-5+tx, 40)
    glVertex2f(-5*math.cos(math.radians(theta))+60*math.sin(math.radians(theta))+tx,-5*math.sin(math.radians(theta))-60*math.cos(math.radians(theta)))
    glEnd()

def water():
    glColor3f(.2,.5,1)
    glBegin(GL_POLYGON)
    glVertex2f(window,-50)
    glVertex2f(-window,-50)
    glVertex2f(-window, -window)
    glVertex2f(window,-window)
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    boat()
    water()
    row()
    glFlush()
    glutSwapBuffers()

def animate(temp):
    global theta,DIR,tx
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))

    if(theta>40):
        DIR=1
    if(theta<-40):
        DIR=0

    if(DIR==1):
        theta-=.8
    else:
        theta+=.8

    if(tx==500):
        tx=-window

    tx+=1


def main():
    glutInit()
    glutInitWindowPosition(50,50)
    glutInitWindowSize(window,window)
    glutCreateWindow("Boat Rowing")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    init_disp()
    glutMainLoop()

main()