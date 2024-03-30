# Asteroids Game

This project is an implementation of the classic Asteroids arcade game in Python using the Pygame library. The game features a player-controlled spaceship navigating through an asteroid field, shooting asteroids, and avoiding collisions. Additionally, it includes database connectivity to store player information and high scores.

## Description

The game window is set to 800x800 pixels and features a space-themed background with player-controlled spaceship graphics. Asteroids of varying sizes randomly spawn and move across the screen, and the player's objective is to destroy them while avoiding collisions. Stars and alien ships also appear sporadically, adding to the game's complexity.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/delisha02/Asteroid-Game.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Asteroid-Game
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the game:

    ```bash
    python main.py
    ```

2. Use the arrow keys to control the spaceship:
   - LEFT arrow: Rotate the spaceship counter-clockwise.
   - RIGHT arrow: Rotate the spaceship clockwise.
   - UP arrow: Move the spaceship forward.

3. Press the SPACEBAR to shoot bullets and destroy asteroids.

4. Press the 'M' key to toggle sound effects on/off.

5. Press the 'TAB' key to play again after game over.

6. When prompted, enter your name and press 'Enter' to save your score to the database.

## Database Connectivity

The game includes functions to interact with a MySQL database for storing player information and high scores. The `connect.py` file contains functions for connecting to the database, inserting player information, updating high scores, and more.

## Credits

- Pygame library for game development.
- Sound effects and images obtained from [araboy24/AsteroidsTut](https://github.com/araboy24/AsteroidsTut).
- Inspiration and assets from the original Asteroids arcade game.
