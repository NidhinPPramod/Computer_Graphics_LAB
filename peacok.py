from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

window=500
theta=0
DIR=0

def initDisp():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(2)
    gluOrtho2D(-window,window,-window,window)

def body():
    glColor3f(1.0,0.0,0.0)
    i=0
    xc=0
    yc=-100
    glPointSize(1.5)
    glBegin(GL_POINTS)
    while i<6.28:
        glVertex2f(100*math.cos(i)+xc,100*math.sin(i)+yc)
        i+=.01
    glEnd()

def head():
    glColor3f(1.0,0.0,0.0)
    glPointSize(1.5)
    glBegin(GL_POLYGON)
    glVertex2f(0, -75)
    glVertex2f(50, -100)
    glVertex2f(0, -175)
    glVertex2f(-50, -100)
    glEnd()
   

def eye():
    glColor3f(1.0,1.0,1.0)
    glPointSize(8)
    glBegin(GL_POINTS)
    glVertex(80,-80)
    glVertex(-80,-80)
    glEnd()

def peeli():
    glPointSize(3)
    glColor3f(0.0,0.5,0.5)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(300*math.cos(math.radians(theta))-5*math.sin(math.radians(theta)),300*math.sin(math.radians(theta))+5*math.cos(math.radians(theta)))
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(-300*math.cos(math.radians(theta))+5*math.sin(math.radians(theta)),300*math.sin(math.radians(theta))+5*math.cos(math.radians(theta)))
    glEnd()


def draw():
    body()
    head()
    eye()
    peeli()
    glFlush()
    glutSwapBuffers()

def animate(temp):
    global theta,DIR
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))
    
    if(DIR==0):
        theta+=.8
    else:
        theta-=.8

    if(theta>90):
        DIR=1
        glClear(GL_COLOR_BUFFER_BIT)
    else:
        DIR=0
        
    


def main():
    glutInit()
    glutInitWindowPosition(50,50)
    glutInitWindowSize(window,window)
    glutCreateWindow("Peacock")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    initDisp()
    glutMainLoop()

main()