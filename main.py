"""
Demo of configuation spaces and robot arm linkages for
Elementary Applied Topology, Spring 2019

@authors Saveliy Yusufov and Kohtaro Yamakawa
"""

import json
import queue
import subprocess

import pygame
from robot import Robot
from network import Server


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the height and width constants
WIDTH = 600
HEIGHT = 400

if __name__ == "__main__":
    pygame.init()

    # Set the width and height of the screen [width, height]
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Configuration Space Visualization Tool")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    data_queue = queue.Queue()
    _ = Server("localhost", 10000, data_queue)

    ALPHA = 0
    THETA = 0
    RADIUS = 30
    ORIGIN_X = WIDTH // 2
    ORIGIN_Y = HEIGHT // 2
    robot = Robot((ORIGIN_X, ORIGIN_Y), RADIUS)

    # Start the scatterplot process
    subprocess.Popen(["python", "plot.py"])

    # Main game loop
    while not done:

        # Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_LEFT]:
            ALPHA -= 1
        if keys[pygame.K_RIGHT]:
            ALPHA += 1
        if keys[pygame.K_UP]:
            THETA += 1
        if keys[pygame.K_DOWN]:
            THETA -= 1

        # Visualization logic
        ALPHA %= 360
        THETA %= 360

        robot.update_alpha(ALPHA)
        robot.update_theta(THETA)
        robot.update_link1_pos()
        robot.update_link2_pos()
        current_pos = robot.get_pos()
        data_queue.put(json.dumps(current_pos))

        # Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # Background image
        screen.fill(WHITE)

        # Drawing code should go here
        robot_base = pygame.draw.circle(screen, BLACK, (ORIGIN_X, ORIGIN_Y), RADIUS)
        link1 = pygame.draw.line(screen, GREEN, robot.link1.start, robot.link1.end, 10)
        link2 = pygame.draw.line(screen, RED, robot.link2.start, robot.link2.end, 10)

        # Update the screen with what we've drawn.
        pygame.display.update([robot_base, link1, link2])

        # Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()
