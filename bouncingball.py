from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

window=500
xc=-window+50
yc=0
i=0
amp=200

def initdisp():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(3)
    gluOrtho2D(-window,window,-window,window)

def circle():
    glBegin(GL_LINES)
    theta=0
    while theta<6.28:
        glVertex2f(xc,yc)
        x=50*math.cos(theta)+xc
        y=50*math.sin(theta)+yc
        theta+=.01
        glVertex2f(x, y)
    glEnd()

def line():
    glBegin(GL_LINES)
    glVertex2f(-window,250)
    glVertex2f(window,250)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(-window,-50)
    glVertex2f(window,-50)
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    circle()
    line()
    glFlush()
    glutSwapBuffers()


def animate(temp):
    global yc,i,xc,amp
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))
    
    
    yc=(amp)*math.sin(math.radians(i))
    amp-=.25
    xc+=2
    i=i+1

    if (i>180):
        i=0
    if(xc>window):
        xc=-window
    if(yc<0):
        yc=0

        

def main():
    glutInit()
    glutInitWindowSize(window,window)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Bouncing Ball")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    initdisp()
    glutMainLoop()

main()