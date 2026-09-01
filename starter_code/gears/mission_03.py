"""Demo mission: follow a dark line using both color sensors.

This example intentionally uses the two sensors as a balanced line follower:
- the left sensor detects the line edge on one side
- the right sensor detects the line edge on the other side
- the robot steers toward the side with the stronger light reading

It is designed for the Gears robot template where the color sensors are mounted
on the left and right front sides and the DriveBase is configured in robot.py.
"""

from pybricks.tools import wait
from robot import Robot


LINE_THRESHOLD = 35
BASE_SPEED = 150
TURN_GAIN = 3.0
MAX_TURN_RATE = 80


def line_follow_demo(r, distance_mm=500):
    """Drive forward a set distance while keeping the robot centered on a line."""
    r.drive_base.reset()
    print(r.left_color.reflection())
    print(r.right_color.reflection())
    while abs(r.drive_base.distance()) < abs(distance_mm):
        left_reflection = r.left_color.reflection()
        right_reflection = r.right_color.reflection()

        error = left_reflection - right_reflection
        drive_speed = BASE_SPEED
        turn_rate = max(-MAX_TURN_RATE, min(MAX_TURN_RATE, error * TURN_GAIN))

        r.drive_base.drive(drive_speed, turn_rate)
        wait(20)

    r.drive_base.stop()


def mission_03(r):
    """Small demo mission that shows two-sensor line following."""
    r.drive_base.settings(170, 500, 180, 360)
    line_follow_demo(r, distance_mm=2400)


if __name__ == "__main__":
    mission_03(Robot())