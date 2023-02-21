from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

Window_size=720

def clearScreen():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-1.0,1.0,-1.0,1.0)


def draw_triangle():
    global x1,y1,x2,y2,x3,y3
    x1=float(input("Enter x1:"))
    x2=float(input("Enter x2:"))
    x3=float(input("Enter x3:"))
    y1=float(input("Enter y1:"))
    y2=float(input("Enter y2:"))
    y3=float(input("Enter y3:"))
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0, 0)
    glPointSize(5)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()

def translate():
    draw_triangle()
    xinc=float(input("Change in x?"))
    yinc=float(input("Change in y?"))
    glColor3f(0.0,1.0, 0)
    glPointSize(5)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1+xinc, y1+yinc)
    glVertex2f(x2+xinc, y2+yinc)
    glVertex2f(x3+xinc, y3+yinc)
    glEnd()
    glFlush()

def rotate():
    draw_triangle()
    deg=int(input("Angle to be rotated(degree)?"))
    angle=(3.14/180)*deg
    glColor3f(0.0,1.0, 0)
    glPointSize(5)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1*math.cos(angle)-y1*math.sin(angle), x1*math.sin(angle)+y1*math.cos(angle))
    glVertex2f(x2*math.cos(angle)-y2*math.sin(angle), x2*math.sin(angle)+y2*math.cos(angle))
    glVertex2f(x3*math.cos(angle)-y3*math.sin(angle), x3*math.sin(angle)+y3*math.cos(angle))
    glEnd()
    glFlush()

def scaling():
    draw_triangle()
    scalx=float(input("Enter x scale factor"))
    scaly=float(input("Enter y scale factor"))
    glColor3f(0.0,1.0, 0)
    glPointSize(5)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1*scalx,y1*scaly)
    glVertex2f(x2*scalx,y2*scaly)
    glVertex2f(x3*scalx,y3*scaly)
    glEnd()
    glFlush()

def reflection():
    draw_triangle()
    glColor3f(0.0,1.0, 0)
    glPointSize(5)
    case=int(input("...Menu...\n1.About X axis\n2.About Yaxis\n3.About origin\n4.About X=Y\n5.About X=-Y"))
    if case ==1:
        glBegin(GL_TRIANGLES)
        glVertex2f(x1,-y1)
        glVertex2f(x2,-y2)
        glVertex2f(x3,-y3)
        glEnd()
    elif case ==2:
        glBegin(GL_TRIANGLES)
        glVertex2f(-x1,y1)
        glVertex2f(-x2,y2)
        glVertex2f(-x3,y3)
        glEnd()
    elif case ==3:
        glBegin(GL_TRIANGLES)
        glVertex2f(-x1,-y1)
        glVertex2f(-x2,-y2)
        glVertex2f(-x3,-y3)
        glEnd()
    elif case ==4:
        glBegin(GL_TRIANGLES)
        glVertex2f(y1,x1)
        glVertex2f(y2,x2)
        glVertex2f(y3,x3)
    elif case ==5:
        glBegin(GL_TRIANGLES)
        glVertex2f(-y1,-x1)
        glVertex2f(-y2,-x2)
        glVertex2f(-y3,-x3)
        glEnd()

    glFlush()

def shearing():
    draw_triangle()
    glColor3f(0.0,1.0, 0)
    glPointSize(5)
    shx=float(input("Enter Shear x factor"))
    shy=float(input("Enter Shear y factor"))
    option=int(input("...Menu...\n1.X-shear\n2.Y-Shear\n3.X-Y shear\n"))
    if option ==1:
        glBegin(GL_TRIANGLES)
        glVertex2f(x1+y1*shx,y1)
        glVertex2f(x2+y2*shx,y2)
        glVertex2f(x3+y3*shx,y3)
        glEnd()
    elif option ==2:
        glBegin(GL_TRIANGLES)
        glVertex2f(x1,y1+x1*shy)
        glVertex2f(x2,y2+x2*shy)
        glVertex2f(x3,y3+x3*shy)
        glEnd()
    elif option ==3:
        glBegin(GL_TRIANGLES)
        glVertex2f(x1+y1*shx,y1+x1*shy)
        glVertex2f(x2+y2*shx,y2+x2*shy)
        glVertex2f(x3+y3*shx,y3+x3*shy)
        glEnd()
    glFlush()


def main():
    glutInit()
    glutInitWindowSize(Window_size,Window_size)
    glutInitDisplayMode(GLUT_SINGLE| GLUT_RGBA)
    glutCreateWindow("2D Transformation")
    choice=int(input("...Menu...\n1.Translation\n2.Rotation\n3.Scaling\n4.Reflection\n5.Shearing"))
    if choice==1:
        glutDisplayFunc(translate)
    elif choice ==2:
        glutDisplayFunc(rotate)
    elif choice ==3:
        glutDisplayFunc(scaling)
    elif choice ==4:
        glutDisplayFunc(reflection)
    elif choice ==5:
        glutDisplayFunc(shearing)

    clearScreen()
    glutMainLoop()

main()