"""
Demo of configuation spaces and robot arm linkages for
Elementary Applied Topology, Spring 2019

@authors Saveliy Yusufov and Kohtaro Yamakawa
"""

import math

import pygame


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
WIDTH = 800
HEIGHT = 600

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

ANGLE = 0
THETA = math.radians(ANGLE)
RADIUS = 30
START_X = (WIDTH // 2)
START_Y = (HEIGHT // 2)
linkage = {"start": [START_X, START_Y], "end": [500*math.cos(THETA), 400*math.sin(THETA)]}


# Main game loop
while not done:

    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Game logic

    # Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # Drawing code should go here
    pygame.draw.circle(screen, BLACK, (WIDTH//2, HEIGHT//2), RADIUS)
    pygame.draw.line(screen, GREEN, linkage["start"], linkage["end"], 10)

    if ANGLE == 360:
        ANGLE = 0
    else:
        ANGLE += 1

    THETA = math.radians(ANGLE)
    linkage["end"] = [START_X + 2*RADIUS*math.cos(THETA), START_Y+2*RADIUS*math.sin(THETA)]
    print(linkage)

    # Update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
