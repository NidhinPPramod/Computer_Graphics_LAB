from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math


WINDOW_SIZE=500
angle=0
def init_display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    glPointSize(2.0)
    gluOrtho2D(-500.0,500.0,500.0,-500.0)

def midpoint_ellipse():
    glBegin(GL_POINTS)
    global yr,xr
    global x,y
    x=0
    y =yr
   
   #initial decision parameter Region1
    p=((yr*yr)-(xr*xr*yr)+(.25*xr*xr))

    dx = 2 * yr * yr * x;
    dy = 2 * xr * xr * y;

    while dx < dy :

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

        plot_symmetric(x, y)
    # Decision parameter of region 2
    p2 = (((yr * yr) * ((x + 0.5) * (x + 0.5))) +
          ((xr * xr) * ((y - 1) * (y - 1))) -
           (xr * xr * yr * yr));      

    while y>0:

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
        plot_symmetric(x, y)

    glEnd()


def plot_symmetric(x,y):
    global xc,yc,angle
    glVertex2f((xc+x)*math.cos(math.radians(angle))-(yc+y)*math.sin(math.radians(angle)), (xc+x)*math.sin(math.radians(angle))+(yc+y)*math.cos(math.radians(angle)))
    glVertex2f((xc+x)*math.cos(math.radians(angle))-(yc-y)*math.sin(math.radians(angle)), (xc+x)*math.sin(math.radians(angle))+(yc-y)*math.cos(math.radians(angle)))
    glVertex2f((xc-x)*math.cos(math.radians(angle))-(yc+y)*math.sin(math.radians(angle)), (xc-x)*math.sin(math.radians(angle))+(yc+y)*math.cos(math.radians(angle)))
    glVertex2f((xc-x)*math.cos(math.radians(angle))-(yc-y)*math.sin(math.radians(angle)), (xc-x)*math.sin(math.radians(angle))+(yc-y)*math.cos(math.radians(angle)))


def drawLine():
    global xc,yc,x,y
    glBegin(GL_LINES)
    glVertex2f(xc, yc)
    glVertex2f((xc+x)*math.cos(math.radians(angle))-(yc+y)*math.sin(math.radians(angle)),(xc+x)*math.sin(math.radians(angle))+(yc+y)*math.cos(math.radians(angle)))
    glEnd()

def draw():
    global x,y,angle
    glClear(GL_COLOR_BUFFER_BIT)
    midpoint_ellipse()
    glutSwapBuffers()
    

def animate(temp):
    global x,y,angle
    
    glutPostRedisplay()
    glutTimerFunc(int(10000/60),animate,int(0))
    if (angle>=360):
        angle=0
    angle+=10



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
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    init_display()
    glutMainLoop()

main()