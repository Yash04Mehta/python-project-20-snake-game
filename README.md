# 🐍 The Basilisk's Path – Snake Movement Engine

## 📌 Project Overview

**The Basilisk's Path** is the movement engine for a classic Snake Game built using **Python Turtle Graphics** and **Object-Oriented Programming (OOP)** principles.

This version focuses on implementing the **core snake movement system**, including keyboard control, segment-follow logic, and smooth animation updates.

It serves as the foundation for future features like:

* Food system
* Score tracking
* Collision detection
* Snake growth mechanics
* Game over logic

---

## 🧠 Concepts Practiced

This project demonstrates the following programming concepts:

* Object-Oriented Programming (OOP)
* Class creation and initialization
* Lists storing object instances
* Keyboard event handling
* Screen animation loop
* Coordinate-based movement logic
* Preventing reverse-direction movement (classic Snake rule)

---

## 📁 Project Structure

### main.py

Responsible for:

* Creating the game window
* Running the animation loop
* Listening for keyboard input
* Updating the screen continuously

### snake.py

Contains the `Snake` class which handles:

* Creating the snake body
* Moving the snake forward
* Updating segment positions
* Managing direction controls
* Preventing reverse turns

---

## 🎮 Controls

| Key           | Action     |
| ------------- | ---------- |
| ↑ Up Arrow    | Move Up    |
| ↓ Down Arrow  | Move Down  |
| ← Left Arrow  | Move Left  |
| → Right Arrow | Move Right |

Reverse movement is blocked to maintain authentic Snake gameplay behavior.

---

## ⚙️ How Movement Works

Each frame of the game loop:

1. The screen refreshes
2. Each segment moves to the position of the segment ahead
3. The head moves forward by a fixed distance
4. Keyboard input updates direction safely

This creates a smooth snake-following motion effect.

---

## 🚀 How to Run the Project

Make sure Python 3 is installed.

Run the program using:

```
python main.py
```

Use the arrow keys to control the snake.

Click anywhere inside the window to exit the game.

---

## 🛠 Features Implemented

✔ Snake body creation

✔ Continuous movement loop

✔ Keyboard direction control

✔ Reverse-direction prevention logic

✔ Segment-follow animation system

✔ Clean OOP-based structure

---

## 📈 Planned Enhancements

Upcoming upgrades for the full Snake Game:

* Food spawning system
* Scoreboard implementation
* Snake length increase after eating food
* Wall collision detection
* Self-collision detection
* Game restart functionality

---

## 🎯 Learning Outcome

By building this project, you practice:

* Structuring game logic using classes
* Managing multiple object instances
* Implementing real-time keyboard input
* Designing animation loops with Turtle graphics
* Preparing scalable architecture for game expansion

This project forms the movement backbone of a complete Snake Game.

---

## Tech Stack

Python (Intermediate Level)
