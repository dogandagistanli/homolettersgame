import pygame
import os
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode([500, 500])

# Load the images
image_path = "sa.png"
image = pygame.image.load(image_path)
image2 = pygame.image.load("images.jpg")

# Get the rectangle for the images
image_rect = image.get_rect(topleft=(50, 50))  # Place the image at (50, 50)
image2_rect = image2.get_rect(topleft=(150, 100))  # Place image2 at (150, 100)

# Variable to track which image is currently displayed
current_image = image2

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            # Check if the mouse click happened on image2
            if event.button == 1 and image2_rect.collidepoint(event.pos):
                # Switch the currently displayed image
                current_image = image

    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Blit the current image onto the screen
    screen.blit(current_image, current_image.get_rect(center=(250, 250)))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
