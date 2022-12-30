from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


WINDOW_SIZE=500

def init_display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    glPointSize(5.0)
    gluOrtho2D(-100.0,100.0,100.0,-100.0)

def midpoint_ellipse():
    glBegin(GL_POINTS)
    global xc,yc,yr,xr
    x=0
    y =yr
   
   #initial decision parameter Region1
    p=((yr*yr)-(xr*xr*yr)+(.25*xr*xr))

    dx = 2 * yr * yr * x;
    dy = 2 * xr * xr * y;

    while dx < dy :
        plot_symmetric(x, y)

        if (p < 0):
            x += 1;
            dx = dx + (2 * yr * yr);
            p = p + dx + (yr * yr);
        else:
            x += 1;
            y -= 1;
            dx = dx + (2 * yr * yr);
            dy = dy - (2 * xr * xr);
            p = p + dx - dy + (yr * yr);

    # Decision parameter of region 2
    p2 = (((yr * yr) * ((x + 0.5) * (x + 0.5))) +
          ((xr * xr) * ((y - 1) * (y - 1))) -
           (xr * xr * yr * yr));      

    while y>0:
        plot_symmetric(x, y)

        if (p2 > 0):
            y -= 1;
            dy = dy - (2 * xr * xr);
            p2 =p2 + (xr * xr) - dy;
        else:
            y -= 1;
            x += 1;
            dx = dx + (2 * yr * yr);
            dy = dy - (2 * xr * xr);
            p2 = p2 + dx - dy + (xr * xr);

    glEnd()
    glFlush()

def plot_symmetric(x,y):
    global xc,yc
    glVertex2f(xc+x, yc+y)
    glVertex2f(xc+x, yc-y)
    glVertex2f(xc-x, yc+y)
    glVertex2f(xc-x, yc-y)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    glutInitWindowPosition(50, 50)
    global xc, yc, xr,yr
    xc = int(input("Enter x coordinate of the centre "))
    yc = int(input("Enter y coordinate of the centre "))
    xr = int(input("Enter length of radius along x axis "))  
    yr = int(input("Enter length of radius along y axis"))  
    glutCreateWindow("ellipse")
    init_display()
    glutDisplayFunc(midpoint_ellipse) 
    glutMainLoop()

main()