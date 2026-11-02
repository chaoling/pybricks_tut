"""Gears single-file lab. Select Double Sensor Line Follower.
S1 is the LEFT sensor; S2 is the RIGHT sensor, viewed from the robot.
Start facing along the stripe, with the line centered between the sensors.
Compare both sensors on black and white in Lab 1 before using raw differences.
This is a bounded trial, not an automatic lap or finish detector.
"""
import time
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

MODE = "bang"                 # Lab 3: change to "p"
SPEED = 100                   # mm/s
KP = 1.0                     # deg/s per reflection point
TURN = 45                    # deg/s, for bang-bang only
MAX_TURN = 120               # deg/s
LIMIT_MM = 1200              # odometer limit, not a finish sensor
TIMEOUT_S = 20               # elapsed wall time, not loop count

left = Motor(Port.A)
right = Motor(Port.B)
sensor1 = ColorSensor(Port.S1)  # left
sensor2 = ColorSensor(Port.S2)  # right
base = DriveBase(left, right, 56, 152)
base.reset()
start = time.time()
reason = "time limit"
try:
    while time.time() - start < TIMEOUT_S:
        if abs(base.distance()) >= LIMIT_MM:
            reason = "distance limit"
            break
        error = sensor1.reflection() - sensor2.reflection()
        if MODE == "bang":
            correction = TURN if error > 0 else -TURN if error < 0 else 0
        elif MODE == "p":
            correction = KP * error
        else:
            raise ValueError("Use MODE = 'bang' or 'p'")
        correction = max(-MAX_TURN, min(MAX_TURN, correction))
        base.drive(SPEED, correction)
        wait(10)
finally:
    base.stop()
print("Stopped:", reason)
print("Elapsed seconds:", time.time() - start)
print("Odometer mm:", base.distance())
