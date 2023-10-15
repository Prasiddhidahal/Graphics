from OpenGL.GL import *
import pygame
from pygame.locals import *

# Set up OpenGL context and window
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glOrtho(0, 800, 0, 600, -1, 1)

# Line endpoints
x1, y1 = 100, 200
x2, y2 = 300, 500

# Bresenham's Line Drawing Algorithm
dx = (x2 - x1)
dy = (y2 - y1)
slope = dy / dx

if slope >= 1:
    p0 = 2 * dx - dy
    xi, yi, pi = x1, y1, p0  # Initialize xi, yi, and pi

    glBegin(GL_POINTS)
    glVertex2f(xi, yi)  # Plot the starting point

    for x in range(x1, x2):
        if pi >= 0:
            yi += 1
            pi += 2 * dx - dy
        else:
            pi += 2 * dx

        xi += 1
        glVertex2f(xi, yi)  # Plot the current point

    glEnd()

else:
    p0 = 2 * dy - dx
    xi, yi, pi = x1, y1, p0  # Initialize xi, yi, and pi

    glBegin(GL_POINTS)
    glVertex2f(xi, yi)  # Plot the starting point

    for y in range(y1, y2):
        if pi >= 0:
            xi += 1
            pi += 2 * dy - dx
        else:
            pi += 2 * dy

        yi += 1
        glVertex2f(xi, yi)  # Plot the current point

    glEnd()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.flip()
display.flip()
