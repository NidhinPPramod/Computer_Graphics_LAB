from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import numpy as np

window_size=800
sys.setrecursionlimit(1000000)
point_size=7


def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(0,window_size,window_size,0)
    glColor3f(1,0,0)
    glPointSize(point_size)



def midpoint_ellipse():
    global ry,rx
    x=0
    y=ry
    glPointSize(10)
    glBegin(GL_POINTS)
    p1=((ry*ry)+(.25*rx*rx)-(ry*rx*rx))

    dx=2*ry*ry*x
    dy=2*rx*rx*y

    while dx<dy:
        plotsymmetric(x, y)
        if p1<0:
            x=x+1
            dx=dx+2*(ry*ry)
            p1=p1+dx+(ry*ry)
        else:
            x=x+1
            y=y-1
            dx=dx+2*(ry*ry)
            dy=dy-2*(rx*rx)
            p1=p1+dx-dy+(ry*ry)

    p2=((ry*ry)*((x+.5)*(x+.5))+((rx*rx)*(y-1)*(y-1))-(rx*rx*ry*ry))

    while y>0:
        plotsymmetric(x, y)
        if p2>0:
            y=y-1
            glVertex2f(*translate_origin(x+xc, y+yc))
            dy=dy-2*(rx*rx)
            p2=p2-dy+(rx*rx)
        else:
            y=y-1
            x=x+1
            glVertex2f(*translate_origin(x+xc, y+yc))
            dx=dx+2*(ry*ry)
            dy=dy-2*(rx*rx)
            p2=p2+dx-dy+(rx*rx)

    glEnd()
    glFlush()


def plotsymmetric(x,y):
    global xc,yc
    glVertex2f(*translate_origin(xc+x,yc+y))
    glVertex2f(*translate_origin(xc+x,yc-y))
    glVertex2f(*translate_origin(xc-x,yc+y))
    glVertex2f(*translate_origin(xc-x,yc-y))

def translate_origin(x,y):
    return x+window_size/2,y+window_size/2


def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        flood_fill(x, y, [0, 1, .5], get_pixel(x, y))

def flood_fill(x, y, new_color, old_color):
    color = get_pixel(x, y)
    if all(color == old_color):
        setpixel(x, y, new_color)
        flood_fill(x + point_size, y, new_color, old_color)
        flood_fill(x, y + point_size, new_color, old_color)
        flood_fill(x - point_size, y, new_color, old_color)
        flood_fill(x, y - point_size, new_color, old_color)

def get_pixel(x,y):
    pixel=glReadPixels(x, window_size-y, 1, 1, GL_RGB,GL_FLOAT)
    return np.array([round(x, 1) for x in pixel[0][0]])

def setpixel(x,y,fill_color=(0,0,0)):
    glColor3f(*fill_color)
    glPointSize(point_size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowPosition(0,0)
    glutInitWindowSize(window_size,window_size)
    global xc,yc,ry,rx
    xc=int(input("Enter Centre x coordinates"))
    yc=int(input("Enter Centre y coordinates"))
    rx=int(input("Enter Radius along x axis"))
    ry=int(input("Enter radius along y axis"))
    glutCreateWindow("Ellipse and Transformations")
    init()
    choice=int(input("Menu\n--------\n1.Flood fill\n2.Scaling\n3.Rotate\n"))
    if choice==1:
        glutDisplayFunc(midpoint_ellipse)
        glutMouseFunc(mouse_click)
        print("CLICK ON THE POINT WHERE BOUNDARY FILL TO BE DONE!!")       
    glutMainLoop()

main()