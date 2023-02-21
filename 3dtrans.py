from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import cos,sin,radians as rad
window_size=500
x1=0
y1=0
z1=0
x2=0
y2=.1
z2=0
x3=.3
y3=0
z3=.3
def plot_points():
	global x1,y1,z1,x2,y2,z2,x3,y3,z3
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,1,0)
	glBegin(GL_POLYGON)
	glVertex3f(x1,y1,z1)
	glVertex3f(x2,y2,z2)
	glVertex3f(x3,y3,z3)
	glEnd()
	glFlush()
	option=int(input("enter \n 1-translation \n 2-rotation \n 3-scaling \n 4-exit \n"))
	if option==1:
		x=int(input("enter x inc:"))/window_size
		y=int(input("enter y inc:"))/window_size
		z=int(input("enter z inc:"))/window_size
		x1=x1+x
		x2=x2+x
		x3=x3+x
		y1=y1+y
		y2=y2+y
		y3=y3+y
		z1=z1+z
		z2=z2+z
		z3=z3+z
	elif option==2:
		choice=int(input("enter\n1.about x-axis\n2.about y-axis\n3.about z-axis\n4.exit\n"))
		
		angle=float(input("enter the angle:"))
		if choice==1:
			y1=y1*cos(rad(angle))-z1*sin(rad(angle))
			y2=y2*cos(rad(angle))-z2*sin(rad(angle))
			y3=y3*cos(rad(angle))-z3*sin(rad(angle))
			z1=y1*sin(rad(angle))+z1*cos(rad(angle))
			z2=y2*sin(rad(angle))+z2*cos(rad(angle))
			z3=y3*sin(rad(angle))+z3*cos(rad(angle))
		if choice==2:
			x1=x1*cos(rad(angle))+z1*sin(rad(angle))
			x2=x2*cos(rad(angle))+z2*sin(rad(angle))
			x3=x3*cos(rad(angle))+z3*sin(rad(angle))
			z1=z1*cos(rad(angle))-x1*sin(rad(angle))
			z2=z2*cos(rad(angle))-x2*sin(rad(angle))
			z3=z3*cos(rad(angle))-x3*sin(rad(angle))
		if choice==3:
			x1=x1*cos(rad(angle))-y1*sin(rad(angle))
			x2=x2*cos(rad(angle))-y2*sin(rad(angle))
			x3=x3*cos(rad(angle))-y3*sin(rad(angle))
			y1=x1*sin(rad(angle))+y1*cos(rad(angle))
			y2=x2*sin(rad(angle))+y2*cos(rad(angle))
			y3=x3*sin(rad(angle))+y3*cos(rad(angle))
	elif option==3:
		delx=int(input("enter the delx:")) 
		dely=int(input("enter the dely:")) 
		delz=int(input("enter the delz:"))
		x1=delx*x1
		x2=delx*x2
		x3=delx*x3		
		y1=dely*y1
		y2=dely*y2
		y3=dely*y3
		z1=delz*z1
		z2=delz*z2
		z3=delz*z3
	
	if option==4:
		exit()
			
			
def main():
	glutInit()
	glutInitWindowSize(window_size,window_size)
	glutInitWindowPosition(50, 50)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutCreateWindow("3-D transformation")
	glutIdleFunc(plot_points)
	glutMainLoop()
main()
