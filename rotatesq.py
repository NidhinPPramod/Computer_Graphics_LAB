from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
window=500
x=100
y=100
theta=0
tx=0
ty=0

def init():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(2.0)
    gluOrtho2D(-window,window,-window,window)

def square():
    glBegin(GL_QUADS)
    glVertex2f(x*math.cos(math.radians(theta))-y*math.sin(math.radians(theta))+tx,x*math.sin(math.radians(theta))+y*math.cos(math.radians(theta))+ty)
    glVertex2f(x*math.cos(math.radians(theta))+y*math.sin(math.radians(theta))+tx,x*math.sin(math.radians(theta))-y*math.cos(math.radians(theta))+ty)
    glVertex2f(-x*math.cos(math.radians(theta))+y*math.sin(math.radians(theta))+tx,-x*math.sin(math.radians(theta))-y*math.cos(math.radians(theta))+ty)
    glVertex2f(-x*math.cos(math.radians(theta))-y*math.sin(math.radians(theta))+tx,-x*math.sin(math.radians(theta))+y*math.cos(math.radians(theta))+ty)
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    square()
    glFlush()
    glutSwapBuffers()

def animate(temp):
    global theta,tx,ty
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))
    if tx==window:
        tx=-window
    tx+=2
    theta+=5
    

def main():
    glutInit()
    glutInitWindowSize(window,window)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Rotating Rectangle")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    init()
    glutMainLoop()

main()