import pygame as pg
import pygame.key
from pygame.locals import *
from OpenGL.GL import *


def rect(fromX, toX, fromY, toY, sc):
    glBegin(GL_QUADS)
    glVertex2f(fromX * sc, fromY * sc)
    glVertex2f(toX * sc, fromY * sc)
    glVertex2f(toX * sc, toY * sc)
    glVertex2f(fromX * sc, toY * sc)
    glEnd()

def draww(size):
    glBegin(GL_QUADS);

    glVertex3f(-size / 2, -size / 2, -size / 2);
    glVertex3f(-size / 2, size / 2, -size / 2);
    glVertex3f(-size / 2, size / 2, size / 2);
    glVertex3f(-size / 2, -size / 2, size / 2);

    glVertex3f(size / 2, -size / 2, -size / 2);
    glVertex3f(size / 2, -size / 2, size / 2);
    glVertex3f(size / 2, size / 2, size / 2);
    glVertex3f(size / 2, size / 2, -size / 2);

    glVertex3f(-size / 2, -size / 2, -size / 2);
    glVertex3f(-size / 2, -size / 2, size / 2);
    glVertex3f(size / 2, -size / 2, size / 2);
    glVertex3f(size / 2, -size / 2, -size / 2);

    glVertex3f(-size / 2, size / 2, -size / 2);
    glVertex3f(-size / 2, size / 2, size / 2);
    glVertex3f(size / 2, size / 2, size / 2);
    glVertex3f(size / 2, size / 2, -size / 2);

    glVertex3f(-size / 2, -size / 2, -size / 2);
    glVertex3f(size / 2, -size / 2, -size / 2);
    glVertex3f(size / 2, size / 2, -size / 2);
    glVertex3f(-size / 2, size / 2, -size / 2);

    glVertex3f(-size / 2, -size / 2, size / 2);
    glVertex3f(size / 2, -size / 2, size / 2);
    glVertex3f(size / 2, size / 2, size / 2);
    glVertex3f(-size / 2, size / 2, size / 2);
    glEnd();

def star(sc):
    x_to_plus = 7.5
    y_to_plus = 2.5
    glColor4f(1.0, 0.0, 0.0, 0.0)
    glPushMatrix()
    glTranslate(0, 0, 0)
    glRotate(-17, 0, 0, 1)
    glTranslate(0, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f((1.2 + x_to_plus) * sc, (1.0 + y_to_plus) * sc)
    glVertex2f((1.2 + x_to_plus) * sc, (1.5 + y_to_plus) * sc)
    glVertex2f((0.0 + x_to_plus) * sc, (1.5 + y_to_plus) * sc)

    glVertex2f((1.2 + x_to_plus) * sc, (1.0 + y_to_plus) * sc)
    glVertex2f((0.6 + x_to_plus) * sc, (0.0 + y_to_plus) * sc)
    glVertex2f((1.6 + x_to_plus) * sc, (0.5 + y_to_plus) * sc)

    glVertex2f((2.0 + x_to_plus) * sc, (1.0 + y_to_plus) * sc)
    glVertex2f((1.6 + x_to_plus) * sc, (0.5 + y_to_plus) * sc)
    glVertex2f((2.5 + x_to_plus) * sc, (0.0 + y_to_plus) * sc)

    glVertex2f((2.0 + x_to_plus) * sc, (1.5 + y_to_plus) * sc)
    glVertex2f((2.0 + x_to_plus) * sc, (1.0 + y_to_plus) * sc)
    glVertex2f((3.0 + x_to_plus) * sc, (1.5 + y_to_plus) * sc)

    glVertex2f((1.2 + x_to_plus) * sc, (1.5 + y_to_plus) * sc)
    glVertex2f((1.6 + x_to_plus) * sc, (2.5 + y_to_plus) * sc)
    glVertex2f((2.0 + x_to_plus) * sc, (1.5 + y_to_plus) * sc)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f((1.2 + x_to_plus) * sc, (1.5 + y_to_plus) * sc)
    glVertex2f((1.2 + x_to_plus) * sc, (1.0 + y_to_plus) * sc)
    glVertex2f((1.6 + x_to_plus) * sc, (0.5 + y_to_plus) * sc)
    glVertex2f((2.0 + x_to_plus) * sc, (1.0 + y_to_plus) * sc)
    glVertex2f((2.0 + x_to_plus) * sc, (1.5 + y_to_plus) * sc)

    glEnd()
    glPopMatrix()

def main():
    pg.init()
    display = (1280, 720)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)

    scale = 1.0 / 16.0
    while True:
        keys = pygame.key.get_pressed()
        glTranslatef(scale * 2.5, scale * 2.5, 0)
        if keys[K_LEFT]:
            glRotate(-0.2, 0, 0, 1)
        if keys[K_RIGHT]:
            glRotate(0.2, 0, 0, 1)
        if keys[K_UP]:
            glRotate(-0.2, 1, 0, 0)
        if keys[K_DOWN]:
            glRotate(0.2, 1, 0, 1)
        glTranslatef(scale * -2.5, scale * -2.5, 0)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor4f(1.0, 1.0, 1.0, 0.0)
        draww(1)
        pygame.display.flip()



main()
