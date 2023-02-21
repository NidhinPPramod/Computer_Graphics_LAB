from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

xc=0
yc=0
r=1

WINDOW_SIZE=500

def init_display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    glPointSize(5.0)
    gluOrtho2D(-100.0,100.0,100.0,-100.0)

def midpoint_circle():
    glBegin(GL_POINTS)
    global r
    x=0
    y =r
    p = 1 - r
    plot_symmetric(x, y)
    while x<y:
        x+=1
        if p<0:
            p=p+2*x+1
        else:
            y-=1
            p+=2*x+1-2*y
        plot_symmetric(x, y)
    glEnd()
    glFlush()

def plot_symmetric(x,y):
    global xc,yc
    glVertex2f(xc+x, yc+y)
    glVertex2f(xc+x, yc-y)
    glVertex2f(xc-x, yc+y)
    glVertex2f(xc-x, yc-y)
    glVertex2f(xc+y, yc+x)
    glVertex2f(xc+y, yc-x)
    glVertex2f(xc-y, yc+x)
    glVertex2f(xc-y, yc-x)



def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    glutInitWindowPosition(50, 50)
    global xc, yc, r
    xc = int(input("Enter x coordinate of the centre "))
    yc = int(input("Enter y coordinate of the centre "))
    r = int(input("Enter length of radius "))  
    glutCreateWindow("circle")
    init_display()
    glutDisplayFunc(midpoint_circle) 
    glutMainLoop()

main()