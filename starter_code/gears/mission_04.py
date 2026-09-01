"""Demo mission: two-sensor PID line follower.

This version uses a simple proportional-integral-derivative controller to keep
both color sensors centered over a dark line.
"""

from pybricks.tools import wait
from robot import Robot


LINE_THRESHOLD = 35
BASE_SPEED = 150
MAX_TURN_RATE = 90

KP = 3.0
KI = 0.04
KD = 0.8


def clamp(value, minimum, maximum):
    return max(minimum, min(maximum, value))


def pid_line_follow(r, distance_mm=500):
    """Follow a dark line for a fixed encoder distance using PID control."""
    r.drive_base.reset()

    last_error = 0
    integral = 0

    while abs(r.drive_base.distance()) < abs(distance_mm):
        left_reflection = r.left_color.reflection()
        right_reflection = r.right_color.reflection()
        error = left_reflection - right_reflection

        integral = clamp(integral + error, -100, 100)
        derivative = error - last_error
        turn_rate = KP * error + KI * integral + KD * derivative
        turn_rate = clamp(turn_rate, -MAX_TURN_RATE, MAX_TURN_RATE)

        r.drive_base.drive(BASE_SPEED, turn_rate)
        last_error = error
        wait(20)

    r.drive_base.stop()


def mission_04(r):
    """PID line-follow demo for the Gears robot."""
    r.drive_base.settings(170, 500, 180, 360)
    pid_line_follow(r, distance_mm=2400)


if __name__ == "__main__":
    mission_04(Robot())