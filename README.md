# Line Follower Robot in Webots

A line-following robot simulated in [Webots](https://cyberbotics.com/), built in Python.
It reads two downward-facing infrared sensors and steers the wheels to stay on a black line.

The repo contains two controllers for the same robot and track:

| Controller | Approach | Behaviour |
|---|---|---|
| `bang_bang` | if / elif rules: line left → turn left, line right → turn right | Works, but zig-zags and must stay slow |
| `pid` *(coming soon)* | PID control on the sensor error | Smooth steering at higher speed |

<!-- Add a demo GIF here once recorded:
![Demo](media/demo.gif)
-->

## How it works (bang-bang controller)

1. **Read** both IR sensors every simulation step.
2. **Compare** the readings: whichever sensor sees the dark line tells the robot which side the line is on.
3. **Steer**: slow or reverse the wheel on that side so the robot turns back onto the line; drive straight when centred.

This is simple and reliable at low speed, but each correction is all-or-nothing, which causes the zig-zag motion. The PID controller fixes this by steering in proportion to how far off the line the robot is.

## Project structure

```
Line_follower_webots/
├── controllers/
│   └── bang_bang/
│       └── bang_bang.py      # if/elif line follower
├── worlds/
│   └── line_follower.wbt     # track + robot
├── media/                    # demo GIFs and plots
└── README.md
```

## Run it

1. Install Webots (tested on R2025a).
2. Clone this repo and open `worlds/line_follower.wbt` in Webots.
3. Press **Play**. The robot's controller is already set to `bang_bang`.

## What I learned

- Reading sensors and driving motors in a Webots control loop
- Turning sensor feedback into steering decisions
- Why rule-based control oscillates, and why that motivates PID

## Next

- PID controller with tuning results (P vs PD vs PID)
- Side-by-side comparison: speed and smoothness of bang-bang vs PID
