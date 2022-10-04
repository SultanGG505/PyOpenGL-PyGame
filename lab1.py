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
        
def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(-0.75,0.0, -3)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        glColor3fv((0,0,0.5))

        rect(0, 16, -4, 5, 0.1)
        
        glColor3fv((1,1,1))

        rect(0, 5,2, 3, 0.1)
        rect(2, 3, 0, 1, 0.1)
        rect(2, 3, 1, 2, 0.1)
        rect(2, 3,3,4, 0.1)
        rect(2, 3,4,5, 0.1)
        
        rect(16,5, 5, 4, 0.1)
        rect(16,5, 3, 2, 0.1)
        rect(16,5, 1, 0, 0.1)
        rect(16, 0, -1, -2, 0.1)
        rect(16, 0, -3, -4, 0.1)

        
        pygame.display.flip()
        pygame.time.wait(1)
main()