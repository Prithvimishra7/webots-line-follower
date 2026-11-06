"""PID line follower for the e-puck (Webots R2025a).

Uses the two ground IR sensors ir0 (left) and ir1 (right) from your world.
Tune Kp first (with Ki = Kd = 0), then add Kd, then Ki only if needed.
"""
from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())
dt = timestep / 1000.0                     # time step in seconds

MAX_SPEED = 6.28                           # e-puck wheel limit (rad/s)
BASE_SPEED = 6                          # forward speed when on the line

# ---------------- PID GAINS (tune these) ----------------
Kp = 4.0       # step 1: start here, raise until it follows, lower if it wobbles
Ki = 0.0       # step 3: only if it always drifts to one side
Kd = 0.0       # step 2: add (e.g. 0.3) to reduce wobble
DIRECTION = 1  # if the robot turns AWAY from the line, change this to -1

# ---------------- devices ----------------
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")
left_motor.setPosition(float("inf"))
right_motor.setPosition(float("inf"))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

left_ir = robot.getDevice("ir0")
right_ir = robot.getDevice("ir1")
left_ir.enable(timestep)
right_ir.enable(timestep)

# ---------------- PID memory ----------------
integral = 0.0
last_error = 0.0

def clamp(value, low, high):
    return max(low, min(high, value))

while robot.step(timestep) != -1:
    left_value = left_ir.getValue()
    right_value = right_ir.getValue()

    # 1. ERROR: how far off-centre we are, scaled to about -1 ... +1
    total = left_value + right_value
    error = (left_value - right_value) / total if total > 0 else 0.0
    error *= DIRECTION

    # 2. PID
    P = Kp * error                                  # react to the error now
    integral = clamp(integral + error * dt, -1, 1)  # remember past error (limited)
    I = Ki * integral
    derivative = (error - last_error) / dt          # how fast the error changes
    D = Kd * derivative
    last_error = error

    correction = P + I + D

    # 3. WHEELS: steer by speeding one wheel up and slowing the other
    left_speed = clamp(BASE_SPEED - correction, -MAX_SPEED, MAX_SPEED)
    right_speed = clamp(BASE_SPEED + correction, -MAX_SPEED, MAX_SPEED)
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)

    print(f"L={left_value:6.2f} R={right_value:6.2f} error={error:+.3f} "
          f"P={P:+.2f} I={I:+.2f} D={D:+.2f}")
