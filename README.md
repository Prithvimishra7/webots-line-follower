# Webots Line Follower Robot | IF-ELSE vs PID

A line-following robot simulation developed using **Webots R2025a and Python**. This project explores how a differential-drive e-puck robot can follow a line using sensor-based control.

The project is intended to compare two approaches to robot navigation: traditional IF-ELSE logic and PID control.

## Project Overview

The robot uses ground sensors to detect the line and adjusts its left and right wheel speeds to follow the path.

**Simulation Software:** Webots R2025a  
**Programming Language:** Python  
**Robot:** e-puck  
**Control Concepts:** Sensor-based navigation, IF-ELSE logic and PID control

## Repository Structure

```text
webots-line-follower/
│
├── controllers/
│   └── if_else_controller/
│       └── if_else_controller.py
│
├── worlds/
│   └── if_else_line_follower_world/
│       ├── Line_follower_if_else.wbt
│       └── Line_follower_PID.wbt
│
├── .gitignore
└── README.md
```

## Implemented Controller

### 1. IF-ELSE Line Follower

File: `controllers/if_else_controller/if_else_controller.py`

Uses conditional statements to make steering decisions based on the ground sensor readings.

The controller checks sensor values and changes the wheel speeds according to predefined conditions.

## Simulation Worlds

| World File | Purpose |
|---|---|
| `Line_follower_if_else.wbt` | IF-ELSE line follower simulation |
| `Line_follower_PID.wbt` | World prepared for PID line follower simulation |

## PID Control – Learning and Development

PID stands for:

- **Proportional (P):** Responds to the current error.
- **Integral (I):** Accounts for accumulated error over time.
- **Derivative (D):** Responds to the rate of change of error.

The goal is to implement PID control and compare its steering behaviour with the IF-ELSE controller.

## Learning Objectives

- Understand how ground sensors detect a line.
- Learn differential-drive robot movement.
- Implement sensor-based navigation using Python.
- Understand IF-ELSE control logic.
- Learn the fundamentals of PID control.
- Explore how wheel-speed adjustments affect robot steering.
- Compare different approaches to line following.

## Technologies Used

- Webots R2025a
- Python 3
- e-puck Robot
- Ground IR Sensors
- Differential Drive
- IF-ELSE Control Logic
- PID Control Concepts

## Future Improvements

- Complete the PID controller implementation.
- Compare IF-ELSE and PID performance.
- Tune PID gains (Kp, Ki and Kd).
- Improve line-following stability.
- Test the robot on different track layouts.

## Author

**Prithvi Mishra**

Robotics & AI Engineering Student

*Learning robotics through simulation, control systems and practical projects.*
