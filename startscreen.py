import pygame
import os
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode([500, 500])

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
