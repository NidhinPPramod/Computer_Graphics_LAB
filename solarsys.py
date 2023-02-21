from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

window=500
theta=0

def init_disp():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(2.0)
    gluOrtho2D(-window,window,-window,window)

def orbit():
    glColor3f(1.0,0.0,0.0)
    theta=0
    rx=250
    ry=150
    glBegin(GL_POINTS)
    while theta<6.28:
        x=rx*math.cos(theta)
        y=ry*math.sin(theta)
        theta+=.01
        glVertex2f(x,y)
    glEnd()


def planet():
    global x,y
    radius=50
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x,y)
    for i in range(0,361,1):
        xp=radius*math.cos(math.radians(i))+x
        yp=radius*math.sin(math.radians(i))+y
        glVertex2f(xp,yp)
    glEnd()



def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    orbit()
    planet()
    glFlush()
    glutSwapBuffers()

def animate(temp):
    global x,y,theta
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))
    
    x=250*math.cos(math.radians(theta))
    y=150*math.sin(math.radians(theta))
    theta+=1
    


    

def main():
    glutInit()
    glutInitWindowPosition(50,50)
    glutInitWindowSize(window,window)
    glutCreateWindow("Solar System")
    init_disp()
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    glutMainLoop()

main()