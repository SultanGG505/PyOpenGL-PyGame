import http

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def drawBubliks():
    # glClearColor(0.48, 0.86, 0.92, 1.0)
    # красный
    glColor3f(1, 0, 0)
    glTranslatef(0.1, -0.02, 0.22)
    glRotatef(90.0, 1.0, 0.0, 0.0)
    glutSolidTorus(0.020, 0.250, 50, 50)
    glRotatef(-90.0, 1.0, 0.0, 0.0)
    glTranslatef(-0.1, 0.02, -0.22)

    # чёрный
    glColor3f(0.0, 0.0, 0.0)
    glTranslatef(-0.6, -0.02, 0.22)
    glRotatef(90.0, 1.0, 0.0, 0.0)
    glutSolidTorus(0.020, 0.250, 50, 50)
    glRotatef(-90.0, 1.0, 0.0, 0.0)
    glTranslatef(0.6, 0.02, -0.22)

    # зелёный
    glColor3f(0, 1, 0)
    glTranslatef(-0.25, -0.02, -0.03)
    glRotatef(90.0, 1.0, 0.0, 0.0)
    glutSolidTorus(0.020, 0.250, 50, 50)
    glRotatef(-90.0, 1.0, 0.0, 0.0)
    glTranslatef(0.25, 0.02, 0.03)

    # жёлтый
    glColor3f(255 / 255, 255 / 255, 0 / 255)
    glTranslatef(-0.95, -0.02, -0.03)
    glRotatef(90.0, 1.0, 0.0, 0.0)
    glutSolidTorus(0.020, 0.250, 50, 50)
    glRotatef(-90.0, 1.0, 0.0, 0.0)
    glTranslatef(0.95, 0.02, 0.03)

    # синий
    glColor3f(0 / 255, 62 / 255, 247 / 255)
    glTranslatef(-1.3, -0.02, 0.22)
    glRotatef(90.0, 1.0, 0.0, 0.0)
    glutSolidTorus(0.020, 0.250, 50, 50)
    glRotatef(-90.0, 1.0, 0.0, 0.0)
    glTranslatef(1.3, 0.02, -0.22)


def drawSphere():
    # голова
    ambient = [0.0215, 0.1745, 0.0215]
    diffuse = [0.07568, 0.61424, 0.07568]
    specular = [0.0, 0.0, 0.0, 1.0]
    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, 0.6 * 128.0)
    # glColor3f(66 / 255, 40 / 255, 0 / 255)
    glTranslatef(-0.55, 0, -0.4 - 0.5)
    glutSolidCube(0.5)
    glTranslatef(0.55, 0, 0.4 + 0.5)


pygame.init()
display = (720, 480)
scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glutInit(sys.argv)
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

x = 1
y = -1
z = 1
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
        if keypress[pygame.K_SPACE]:
            glTranslatef(0, -ms, 0)
        if keypress[pygame.K_LSHIFT]:
            glTranslatef(0, ms, 0)
        if keypress[pygame.K_LEFT]:
            x -= 0.1
        if keypress[pygame.K_RIGHT]:
            x += 0.1
        if keypress[pygame.K_UP]:
            y -= 0.1
            z -= 0.1
        if keypress[pygame.K_DOWN]:
            y += 0.1
            z += 0.1
        if keypress[pygame.K_1]:
            z -= 0.1
        if keypress[pygame.K_2]:
            z += 0.1
        if keypress[pygame.K_BACKSPACE]:
            x = 1
            y = -1
            z = 1

        # apply the left and right rotation
        glRotatef(mouseMove[0] * 0.1, 0.0, 1.0, 0.0)

        # multiply the current matrix by the get the new view matrix and store the final vie matrix
        glMultMatrixf(viewMatrix)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        # apply view matrix
        glPopMatrix()
        glMultMatrixf(viewMatrix)

        glLightfv(GL_LIGHT0, GL_POSITION, [x, y, z, 0])

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()

        drawSphere()

        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

pygame.quit()
