import pygame as pygame
import random as random
import numpy as np

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def rect(fromX, toX, fromY, toY, sc):
    glBegin(GL_QUADS)
    glVertex2f(fromX * sc, fromY * sc)
    glVertex2f(toX * sc, fromY * sc)
    glVertex2f(toX * sc, toY * sc)
    glVertex2f(fromX * sc, toY * sc)
    glEnd()


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
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(-0.75, 0.0, -3)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        scale = 0.1

        glColor4f(1.0, 1.0, 1.0, 0.0)
        rect(0, 8, -4, 5, scale)

        glColor3f(0.0, 1.0, 0.0)
        rect(8, 16, -4, 5, scale)

        star(scale)
        pygame.display.flip()
        pygame.time.wait(1)


main()
