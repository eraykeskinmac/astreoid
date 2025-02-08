# Asteroids Game

A Python implementation of the classic Asteroids arcade game, created as part of the Boot.dev curriculum.

## Description

This is a simple clone of the classic Asteroids game where players control a spaceship and shoot asteroids. The game features:
- Player movement with WASD keys
- Shooting mechanics with spacebar
- Asteroids that split into smaller pieces when shot
- Collision detection
- Game over when player hits an asteroid

## Controls

- W: Move forward
- S: Move backward
- A: Rotate left
- D: Rotate right
- Spacebar: Shoot

## Dependencies

- Python 3.x
- Pygame

## Installation

1. Clone the repository
2. Create a virtual environment (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the game:
   ```bash
   python main.py
   ```

## Project Structure

```
asteroids/
├── main.py           # Main game loop and initialization
├── constants.py      # Game constants and configuration
├── circleshape.py   # Base class for game objects
├── player.py        # Player ship implementation
├── asteroid.py      # Asteroid implementation
├── shot.py          # Bullet implementation
├── asteroidfield.py # Asteroid spawning logic
├── requirements.txt # Project dependencies
└── .gitignore      # Git ignore file
```

## Game Mechanics

The game uses Pygame's sprite system and circle-based collision detection. Key features include:
- Circular collision detection for all game objects
- Asteroids split into smaller pieces when shot
- Player movement with momentum and rotation
- Rate-limited shooting mechanics
- Random asteroid spawning from screen edges

## Acknowledgments

Created as part of the [Boot.dev](https://boot.dev) Python game development curriculum.