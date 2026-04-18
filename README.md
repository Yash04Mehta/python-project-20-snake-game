## 🐍 The Basilisk's Path – A Slytherin-Themed Snake Game

## Project Overview
**The Basilisk's Path** is a themed Snake Game built using **Python Turtle Graphics** and **Object-Oriented Programming (OOP)** principles.
Inspired by the hidden chambers beneath Hogwarts, the player guides the Basilisk through the arena while collecting energy fragments and avoiding collisions with walls and its own body.

This project demonstrates how a classic arcade mechanic can be transformed into a narrative-driven mini game using clean Python architecture.

---

### Concepts Practiced

This project demonstrates:

* Object-Oriented Programming (OOP)
* Class-based game architecture
* Event-driven keyboard input handling
* Screen animation loops using Turtle Graphics
* Segment-follow movement logic
* Dynamic object spawning (food system)
* Collision detection (wall + self)
* State-based gameplay flow
* Intro screen trigger system
* Score tracking with real-time updates

---

### Project Structure

main.py
Controls:

* Game window setup
* Intro screen trigger (Press SPACE to begin)
* Main animation loop
* Collision detection logic
* Player input handling

snake.py
Handles:

* Snake body creation
* Segment-follow movement logic
* Direction control
* Reverse-movement prevention
* Snake growth mechanics

food.py
Responsible for:

* Randomized food spawning
* Position refresh after collection

scoreboard.py
Displays:

* Basilisk Power score
* Game-over message
* Themed UI text rendering

---

### Controls

| Key   | Action         |
| ----- | -------------- |
| ↑     | Move Up        |
| ↓     | Move Down      |
| ←     | Move Left      |
| →     | Move Right     |
| SPACE | Begin the game |

Reverse movement is blocked to preserve classic Snake gameplay behavior.

---

### Gameplay Features Implemented

✔ Intro screen with start trigger

✔ Smooth snake movement system

✔ Snake growth after consuming food

✔ Real-time score tracking ("Basilisk Power")

✔ Wall collision detection

✔ Self-collision detection

✔ Themed Game Over screen

✔ Slytherin-inspired visual palette

✔ Clean modular OOP structure

---

### Theme & Atmosphere

The game reimagines the classic Snake experience through a **Slytherin-inspired aesthetic**, featuring:

* Dark emerald chamber background
* Silver-toned UI text
* Basilisk-themed narrative elements
* Immersive start screen ritual
* Story-style game-over message:

  “The Chamber Falls Silent”

---

### How to Run the Project

Make sure Python 3 is installed.

Run:

python main.py

Press **SPACE** to awaken the Basilisk and begin gameplay.

Use arrow keys to navigate.

---

### Planned Enhancements

Future upgrades may include:

* Restart-game functionality
* Sound effects
* Difficulty scaling (speed increase)
* High-score tracking
* Themed collectible variations
* Animated intro sequence

---

### Learning Outcome

By building this project, you practice:

* Designing modular game architecture
* Managing real-time movement systems
* Implementing collision detection
* Structuring multi-file Python projects
* Creating interactive UI using Turtle graphics
* Transforming classic mechanics into themed gameplay experiences

---

### Tech Stack

Python (Intermediate Level)

Python (Turtle Graphics)

Object-Oriented Programming (OOP)
