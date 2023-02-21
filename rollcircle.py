from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

WINDOW_SIZE=500
xc=WINDOW_SIZE
yc=WINDOW_SIZE
radius=100
angle=0

def initDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    glPointSize(2.0)
    gluOrtho2D(-500.0,500.0,-500.0,500.0)


def roll_circle():
    global xc,yc,radius,angle
    theta=0
    glBegin(GL_POINTS)
    while theta<6.28:
        x=radius*math.cos(theta)+xc
        y=radius*math.sin(theta)+yc
        glVertex2f(x, y)
        theta+=.01
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(xc, yc)
    glVertex2f(radius*math.cos(math.radians(angle))+xc,radius*math.sin(math.radians(angle))+yc)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(WINDOW_SIZE, WINDOW_SIZE)
    glVertex2f(-WINDOW_SIZE,-WINDOW_SIZE)
    glEnd()


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    roll_circle()
    glutSwapBuffers()

def animate(temp):
    global xc,yc,angle
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))

    if xc==-WINDOW_SIZE:
        xc=WINDOW_SIZE
        yc=WINDOW_SIZE
    xc=xc-1
    yc=yc-1

    if(angle>360):
        angle=0
    
    angle+=1
    
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowPosition(50,50)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutCreateWindow("ROLLING BALL")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    initDisplay()
    glutMainLoop()

main()