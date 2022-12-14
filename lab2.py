import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math


def drawRect(fromX, toX, fromY, toY):
    glBegin(GL_QUADS)
    glVertex2f(fromX, fromY)
    glVertex2f(toX, fromY)
    glVertex2f(toX, toY)
    glVertex2f(fromX, toY)
    glEnd()


def drawCube(w, h, z):
    z = -z
    glBegin(GL_POLYGON)
    glVertex3f(-w, -h, z)
    glVertex3f(-w, h, z)
    glVertex3f(w, h, z)
    glVertex3f(w, -h, z)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-w, -h, -z)
    glVertex3f(-w, h, -z)
    glVertex3f(w, h, -z)
    glVertex3f(w, -h, -z)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(-w, -h, -z)
    glVertex3f(-w, h, -z)
    glVertex3f(-w, h, z)
    glVertex3f(-w, -h, z)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(w, -h, -z)
    glVertex3f(w, h, -z)
    glVertex3f(w, h, z)
    glVertex3f(w, -h, z)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(-w, -h, -z)
    glVertex3f(w, -h, -z)
    glVertex3f(w, -h, z)
    glVertex3f(-w, -h, z)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-w, h, -z)
    glVertex3f(w, h, -z)
    glVertex3f(w, h, z)
    glVertex3f(-w, h, z)
    glEnd()


def drawTriangle(h, z):
    z = -z

    glBegin(GL_POLYGON)
    glVertex3f(0, -h, z)
    glVertex3f(0, h, z)
    glVertex3f(0, 0, -0.5 * z)
    glEnd()


def drawCat():
    # основа дома
    glColor4f(1, 0.0, 0, 0)
    glTranslatef(0, 0, 0.0)
    drawCube(0.1, 0.1, 0.1)
    glTranslatef(0, 0, -0.0)

    # окно
    glColor4f(0, 1, 1, 1)
    glTranslatef(-0.105, -0.05, -0.01)
    drawCube(0.01, 0.03, 0.03)
    glTranslatef(0.105, 0.03, 0.01)

    # дверь
    glColor4f(1, 0.5, 0, 0)
    glTranslatef(-0.105, 0.05, -0.01)
    drawCube(0.01, 0.03, 0.07)
    glTranslatef(0.105, -0.05, 0.01)

    # ручка
    glColor3f(0, 0, 0)
    glTranslatef(-0.115, 0.07, -0.01)
    drawCube(0.001, 0.01, 0.01)
    glTranslatef(0.115, -0.07, 0.01)

    # передняя стенка-держатель крыши
    glColor4f(0, 1.0, 0, 0)
    glTranslatef(-0.1, 0.02, 0.16)
    drawTriangle(0.1, 0.06)
    glTranslatef(0.1, -0.02, -0.16)

    # задняя стенка-держатель крыши
    glColor4f(0, 1.0, 0, 0)
    glTranslatef(0.1, 0.02, 0.16)
    drawTriangle(0.1, 0.06)
    glTranslatef(-0.1, -0.02, -0.16)

    # правая часть крыши
    glColor3f(0, 0, 1)
    glTranslatef(-0, -0.02, 0.16)
    glRotatef(41.0, 1.0, 0.0, 0.0)
    drawRect(-0.137, 0.137, -0.1, 0.055)
    glRotatef(-41.0, 1.0, 0.0, 0.0)
    glTranslatef(0, 0.02, -0.16)

    # левая часть крыши
    glColor3f(0, 0, 1)
    glTranslatef(-0, 0.089, 0.13)
    glRotatef(-42.0, 1.0, 0.0, 0.0)
    drawRect(-0.137, 0.137, -0.1, 0.055)
    glRotatef(42.0, 1.0, 0.0, 0.0)
    glTranslatef(0, -0.089, -0.13)


pygame.init()
display = (1200, 900)
scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glShadeModel(GL_SMOOTH)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

sphere = gluNewQuadric()

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()

# init mouse movement and center mouse on screen
displayCenter = [scree.get_size()[i] // 2 for i in range(2)]
mouseMove = [0, 0]
pygame.mouse.set_pos(displayCenter)

pygame.mouse.set_visible(False)
up_down_angle = 0.0
paused = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False
            if event.key == pygame.K_PAUSE or event.key == pygame.K_p:
                paused = not paused
                pygame.mouse.set_pos(displayCenter)
        if not paused:
            if event.type == pygame.MOUSEMOTION:
                mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
            pygame.mouse.set_pos(displayCenter)

    if not paused:
        # get keys
        keypress = pygame.key.get_pressed()
        # mouseMove = pygame.mouse.get_rel()

        # init model view matrix
        glLoadIdentity()

        # apply the look up and down
        up_down_angle += mouseMove[1] * 0.1
        glRotatef(up_down_angle, 1.0, 0.0, 0.0)

        # init the view matrix
        glPushMatrix()
        glLoadIdentity()
        ms = 0.06
        # apply the movment
        if keypress[pygame.K_w]:
            glTranslatef(0, 0, ms)
        if keypress[pygame.K_s]:
            glTranslatef(0, 0, -ms)
        if keypress[pygame.K_d]:
            glTranslatef(-ms, 0, 0)
        if keypress[pygame.K_a]:
            glTranslatef(ms, 0, 0)

        # apply the left and right rotation
        glRotatef(mouseMove[0] * 0.1, 0.0, 1.0, 0.0)

        # multiply the current matrix by the get the new view matrix and store the final vie matrix
        glMultMatrixf(viewMatrix)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        # apply view matrix
        glPopMatrix()
        glMultMatrixf(viewMatrix)

        glLightfv(GL_LIGHT0, GL_POSITION, [1, -1, 1, 0])

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()

        drawCat()

        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

pygame.quit()
