from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np
from math import*
def draw_circle(r = 0.5,xc=0,yc=0,R=1,g=0,b=0):
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, .001):
        x = xc+r * cos(theta)
        y = yc+r * sin(theta)
        glColor(R,g, b)
        glVertex(x, y)
    glEnd()
def draw_line(x1,y1,x2,y2):
    glBegin(GL_LINES)
    glColor(0,0,0)
    glVertex(x1,y1)
    glVertex(x2,y2)
    glEnd()
def draw_line_loop(x1,y1,x2,y2,x3,y3,x4,y4):
    glBegin(GL_LINE_LOOP)
    glColor(0, 0, 0)
    glVertex(x1, y1)
    glVertex(x2, y2)
    glVertex(x3, y3)
    glVertex(x4,y4)

    glEnd()
def draw_poly(x1,y1,x2,y2,x3,y3,x4,y4,r,g,b):
    glBegin(GL_POLYGON)
    glColor(r,g,b)
    glVertex(x1, y1)
    glVertex(x2, y2)
    glVertex(x3, y3)
    glVertex(x4, y4)
    glEnd()

def draw():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 1)
    glColor(1,0,0)
    glColor(1, 0.8, 0.1)
    draw_poly(0.35, 0.35,0.35, -0.35,-0.35, - 0.35,-0.35, 0.35,1, 0.8, 0.1)
    glLineWidth(5)
    draw_line_loop(0.35, 0.35,0.35, -0.35,-0.35, - 0.35,-0.35, 0.35)

    draw_poly(-0.35, -0.2,-0.35, -0.65,-0.6, - 0.65,-0.6, -0.2,.5,.5,.5)
    draw_poly(0.35, -0.2,0.35, -0.65,0.6, - 0.65,0.6,- 0.2,.5, .5, .5)
    draw_line_loop(-0.35, -0.2,-0.35, -0.65,-0.6, - 0.65,-0.6, -0.2)
    draw_line_loop(0.35, -0.2,0.35, -0.65,0.6, - 0.65,0.6, - 0.2)
    draw_poly(.2,.35,-.2,.35,-.2,.45,.2,.45,1, 0.8, 0.1)
    draw_poly(.1, .45, -.1, .45, -.1, .55, .1, .55,1, 0.8, 0.1)
    draw_line_loop(.2,.35,-.2,.35,-.2,.45,.2,.45)
    draw_line_loop(.1, .45, -.1, .45, -.1, .55, .1, .55)
    for y in np.arange(.2, .65, .1):
        draw_line(.35, -y, .55, -y)
    for y in np.arange(.35, .55, .2):
        draw_line(.6, -y, .4, -y)
    for y in np.arange(.2, .65, .1):
        draw_line(-.35, -y, -.55, -y)
    for y in np.arange(.35, .55, .2):
        draw_line(-.6, -y, -.4, -y)
    draw_line(.35,.13,-.35,.13)
    draw_poly(.34,.14,-.34,.14,-0.34, 0.34,0.34, 0.34,0.6,0.7,0.9)
    draw_line(0,.34,0,.14)
    draw_line(.2, .34, 0.2, .1)
    draw_line(-.2, .34, -0.2, .1)
    draw_poly(0.05,.19,.15,.19,.15,.3,.05,.3,0.6,1,0)
    glLineWidth(3)
    draw_line_loop(0.05,.19,.15,.19,.15,.3,.05,.3)
    draw_circle(.03,-.1,.19,0.7,0.10,.2)
    glLineWidth(2)
    draw_line(-.16,.3,-.05,.3)
    draw_line(-.16, .28, -.05, .28)
    draw_line(-.16, .26, -.05, .26)
    glLineWidth(4)
    draw_line(.2, .29, .34, .29)
    draw_line(-.2, .29, -.34, .29)
    draw_poly(.21, .295, .34, .295,.34,.34,.21,.34,0.6,0.5,0.7)
    draw_poly(-.21, .295,- .34, .295,- .34, .34,- .21, .34, 0.6, 0.5, 0.7)

    draw_poly(.15, .13, .4, .13, .4, .23, .15, .232,0.6,0.7,0.9)
    draw_poly(.15, .01, .4, .01, .4, .1, .15, .1, 0.6, 0.7, 0.9)
    draw_line_loop(.15, .13, .4, .13, .4, .23, .15, .23)
    draw_line_loop(.15, .01, .4, .01, .4, .1, .15, .1)

    draw_poly(-.15, .13, - .4, .13, - .4, .23, - .15, .23, 0.6, 0.7, 0.9)
    draw_poly(-.15, .01, -.4, .01, -.4, .1, - .15, .1, 0.6, 0.7, 0.9)
    draw_line_loop(-.15, .13, - .4, .13, - .4, .23, - .15, .23)
    draw_line_loop(-.15, .01, -.4, .01, -.4, .1, - .15, .1)
    draw_poly(.18,.125,.18,.11,.4,.11,.4,.125,.6,.7,.9)
    glLineWidth(2)
    draw_line_loop(.18,.125,.18,.11,.4,.11,.4,.125)
    draw_poly(-.18, .125, -.18, .11, -.4, .11, -.4, .125, .6, .7, .9)
    draw_line_loop(-.18, .125, -.18, .11, -.4, .11, -.4, .125)
    glLineWidth(4)
    draw_line(.25,.23,.25,.13)
    draw_line(.25, .01, .25, .1)
    draw_line(-.25, .23, -.25, .13)
    draw_line(-.25, .01,- .25, .1)

    draw_poly(.3,.17,.36,.17,.36,.08,.3,.08, .6, .7, .9)
    draw_line_loop(.3, .17, .36, .17, .36, .08, .3, .08)

    draw_poly(-.3,   .17, -.36, .17, -.36, .08,- .3, .08, .6, .7, .9)
    draw_line_loop(-.3, .17, -.36, .17, -.36, .08, - .3, .08)



    glBegin(GL_POLYGON)
    glColor(.6, .7, .9)
    glVertex(0,.56 )
    glVertex(.18,.69)
    glVertex(-.18, .69)
    glEnd()
    draw_circle(.1,.18,.69,0,0,0)
    draw_circle(.1, -.18, .69, 0, 0, 0)
    draw_circle(.085, .18, .69, 0.3,0.9,1)
    draw_circle(.085, -.18, .69, 0.3, 0.9, 1)
    draw_circle(.06, .18, .69, 0, 0, 0)
    draw_circle(.05, .18, .69,0.3,0.3,0.5)
    draw_circle(.02, .205, .69,0.4,1,1)
    draw_circle(.06, -.18, .69, 0, 0, 0)
    draw_circle(.05, -.18, .69, 0.3, 0.3, 0.5)
    draw_circle(.02, -.205, .69, 0.4, 1, 1)
    glLineWidth(2.5)
    draw_line(-.1,-.24,-0.01,-.24)
    draw_line(-.1, -.24, -.1, -.19)
    draw_line(-.01, -.24, -0.01, -.19)
    draw_line(-.055, -.24, -0.055, -.19)

    draw_line(.01, -.24, 0.01, -.19)
    draw_line(.05, -.24, 0.05, -.19)
    draw_line(.01, -.215, 0.05, -.215)
    draw_line(.01, -.19, 0.05, -.19)

    draw_line(.065,-.24,.1,-.24)
    draw_line(.065, -.24, .065, -.19)

    draw_line(.11, -.24, .145, -.24)
    draw_line(.11, -.24, .11, -.19)
    draw_line(.155,-.24,.169, -.24)
    draw_line(.18,-.24,.18,-.19)
    draw_line(.18, -.24, .23, -.24)
    draw_line(.18, -.19, .23, -.19)
    draw_line(.18, -.215, .23, -.215)
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"first opengl program")
glutDisplayFunc(draw)
glutMainLoop()

