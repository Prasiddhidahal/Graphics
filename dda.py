from OpenGL.GL import *
import numpy as np
import pygame
from pygame.locals import *

# Set up OpenGL context and window
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glOrtho(0, 800, 0, 600, -1, 1)

# Line endpoints
x1, y1 = 100,200
x2, y2 = 150,150

# Calculate dx and dy
dx = x2 - x1
dy = y2 - y1
# Determine the number of steps
steps = max(abs(dx), abs(dy))

# Calculate increments
x_increment = dx / steps
y_increment = dy / steps

# Initialize starting point
x, y = x1, y1

# Initialize OpenGL
glBegin(GL_POINTS)

# Plot each point along the line
for _ in range(int(steps)):
    glVertex2f(x, y)
    x += x_increment
    y += y_increment

glEnd()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.flip()

    
