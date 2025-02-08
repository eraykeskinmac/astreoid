import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set up player groups
    Player.containers = (updatable, drawable)

    # Set up asteroid groups
    Asteroid.containers = (asteroids, updatable, drawable)

    # Set up shot groups
    Shot.containers = (shots, updatable, drawable)

    # Set up asteroid field
    AsteroidField.containers = (updatable,)

    # Create player in center of screen (will auto-add to groups)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Create asteroid field
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        # Update all objects
        updatable.update(dt)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return

            # Check for collisions between asteroids and shots
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()  # Split or destroy the asteroid
                    shot.kill()       # Remove shot from all groups
                    break  # Stop checking other shots for this asteroid

        # Draw all objects
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
