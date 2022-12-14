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


def drawBear():
    # голова
    glColor3f(66 / 255, 40 / 255, 0 / 255)
    glTranslatef(-0.55, 0, -0.4 - 0.5)
    glutSolidCube(0.5)
    glTranslatef(0.55, 0, 0.4 + 0.5)

    # левое ухо
    glColor3f((66 - 20) / 255, (40 - 20) / 255, 0 / 255)
    glTranslatef(-0.80, 0, -0.16 - 0.5)
    glutSolidCube(0.2)
    glTranslatef(0.80, 0, 0.16 + 0.5)

    # правое ухо
    glColor3f((66 - 20) / 255, (40 - 20) / 255, 0 / 255)
    glTranslatef(-0.30, 0, -0.16 - 0.5)
    glutSolidCube(0.2)
    glTranslatef(0.30, 0, 0.16 + 0.5)

    # левый глаз
    glColor3f(255 / 255, 255 / 255, 255 / 255)
    glTranslatef(-0.65, -0.3, -0.3 - 0.5)
    glutSolidCube(0.1)
    glTranslatef(0.65, 0.3, 0.3 + 0.5)

    # левый зрачок
    glColor3f(0 / 255, 0 / 255, 0 / 255)
    glTranslatef(-0.65, -0.3 - 0.05, -0.3 - 0.5)
    glutSolidCube(0.05)
    glTranslatef(0.65, 0.3 + 0.05, 0.3 + 0.5)

    # правый глаз
    glColor3f(255 / 255, 255 / 255, 255 / 255)
    glTranslatef(-0.45, -0.3, -0.3 - 0.5)
    glutSolidCube(0.1)
    glTranslatef(0.45, 0.3, 0.3 + 0.5)

    # правый зрачок
    glColor3f(0 / 255, 0 / 255, 0 / 255)
    glTranslatef(-0.45, -0.3 - 0.05, -0.3 - 0.5)
    glutSolidCube(0.05)
    glTranslatef(0.45, 0.3 + 0.05, 0.3 + 0.5)

    # что-то возможно похожее на рот

    glColor3f(255 / 255, 0 / 255, 0 / 255)
    glTranslatef(-0.45, -0.25 - 0.05, -0.5 - 0.5)
    glutSolidCube(0.1)
    glTranslatef(0.45, 0.25 + 0.05, 0.5 + 0.5)

    glTranslatef(-0.45 - 0.1, -0.25 - 0.05, -0.5 - 0.5)
    glutSolidCube(0.1)
    glTranslatef(0.45 + 0.1, 0.25 + 0.05, 0.5 + 0.5)

    glTranslatef(-0.45 - 0.1 * 2, -0.25 - 0.05, -0.5 - 0.5)
    glutSolidCube(0.1)
    glTranslatef(0.45 + 0.1 * 2, 0.25 + 0.05, 0.5 + 0.5)

    # шея
    glColor3f(66 / 255, 40 / 255, 0 / 255)
    glTranslatef(-0.55, 0, -0.7 - 0.5)
    glutSolidCube(0.2)
    glTranslatef(0.55, 0, 0.7 + 0.5)

    # нижняя часть туловища
    glColor3f(66 / 255, 40 / 255, 0 / 255)
    glTranslatef(-0.55, 0, -1.5 - 0.5)
    glutSolidCube(0.5)
    glTranslatef(0.55, 0, 1.5 + 0.5)

    # левая нога
    glColor3f(30 / 255, 30 / 255, 30 / 255)
    glTranslatef(-0.75, -0.32, -1.63 - 0.5)
    glutSolidCube(0.125)
    glTranslatef(0.75, 0.32, 1.63 + 0.5)

    # правая нога
    glColor3f(30 / 255, 30 / 255, 30 / 255)
    glTranslatef(-0.35, -0.32, -1.63 - 0.5)
    glutSolidCube(0.125)
    glTranslatef(0.35, 0.32, 1.63 + 0.5)

    # верхняя часть туловища
    glColor3f((66 - 10) / 255, (40 - 10) / 255, 0 / 255)
    glTranslatef(-0.55, 0, -1 - 0.5)
    glutSolidCube(0.5)
    glTranslatef(0.55, 0, 1 + 0.5)

    # левая рука
    glColor3f((66 - 5) / 255, (40 - 5) / 255, 0 / 255)
    glTranslatef(-0.860, 0, -1 - 0.5)
    glutSolidCube(0.125)
    glTranslatef(0.860, 0, 1 + 0.5)

    glTranslatef(-0.985, 0, -1 - 0.5)
    glutSolidCube(0.125)
    glTranslatef(0.986, 0, 1 + 0.5)

    glTranslatef(-0.985 - 0.125, 0, -1 - 0.5)
    glutSolidCube(0.125)
    glTranslatef(0.986 + 0.125, 0, 1 + 0.5)

    # правая рука
    glColor3f((66 - 5) / 255, (40 - 5) / 255, 0 / 255)
    glTranslatef(-0.25, 0, -1 - 0.5)
    glutSolidCube(0.125)
    glTranslatef(0.25, 0, 1 + 0.5)

    glTranslatef(-0.25 + 0.125, 0, -1 - 0.5)
    glutSolidCube(0.125)
    glTranslatef(0.25 - 0.125, 0, 1 + 0.5)

    glTranslatef(-0.25 + 0.125 * 2, 0, -1 - 0.5)
    glutSolidCube(0.125)
    glTranslatef(0.25 - 0.125 * 2, 0, 1 + 0.5)


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
        drawBubliks()
        drawBear()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

pygame.quit()