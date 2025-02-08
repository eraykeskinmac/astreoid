# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# Import everything from the constants.py file
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.init()

    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill screen with black color
        screen.fill("black")

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()