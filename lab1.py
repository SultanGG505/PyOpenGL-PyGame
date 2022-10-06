import pygame as pygame
import random as random
import numpy as np

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def rect(fromX, toX, fromY, toY, scale):
    glBegin(GL_QUADS)
    glVertex2f(fromX * scale, fromY * scale)
    glVertex2f(toX * scale, fromY * scale)
    glVertex2f(toX * scale, toY * scale)
    glVertex2f(fromX * scale, toY * scale)
    glEnd()


def triangle(scale):
    glBegin(GL_TRIANGLES)
    glColor4f(1.0, 0.0, 0.0, 0.0)

    glVertex2f(11.0 * scale, -0.0 * scale)
    glVertex2f(12.0 * scale, 2.0 * scale)
    glVertex2f(13.0 * scale, -0.0 * scale)
    glEnd()
    glBegin(GL_TRIANGLES)
    glColor4f(1.0, 0.0, 0.0, 0.0)

    glVertex2f(7.0 * scale, -0.0 * scale)
    glVertex2f(8.0 * scale, 2.0 * scale)
    glVertex2f(9.0 * scale, -0.0 * scale)
    glEnd()


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

        glColor4f(1.0, 1.0, 1.0, 0.0)
        rect(0, 8, -4, 5, 0.1)
        glColor3f(0.0, 1.0, 0.0)
        rect(8, 16, -4, 5, 0.1)
        triangle(0.1)
        # rect(0, 5, 2, 3, 0.1)
        # rect(2, 3, 0, 1, 0.1)
        # rect(2, 3, 1, 2, 0.1)
        # rect(2, 3, 3, 4, 0.1)
        # rect(2, 3, 4, 5, 0.1)
        #
        # rect(16, 5, 5, 4, 0.1)
        # rect(16, 5, 3, 2, 0.1)
        # rect(16, 5, 1, 0, 0.1)
        # rect(16, 0, -1, -2, 0.1)
        # rect(16, 0, -3, -4, 0.1)

        pygame.display.flip()
        pygame.time.wait(1)


main()
