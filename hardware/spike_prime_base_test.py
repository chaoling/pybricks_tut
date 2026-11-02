"""SPIKE Prime base robot movement test for Pybricks.

Assumed course robot configuration:
    Left drive motor:  Port D, positive direction counterclockwise
    Right drive motor: Port F, positive direction clockwise
    Wheel diameter:    56 mm
    Axle track:        128 mm

Place the robot on the floor with at least 1 meter of clear space before
running. Adjust the ports, directions, and dimensions for your own build.
"""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Color, Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait


# ---------- Robot configuration ----------

LEFT_DRIVE_PORT = Port.D
RIGHT_DRIVE_PORT = Port.F

WHEEL_DIAMETER_MM = 56
AXLE_TRACK_MM = 128

STRAIGHT_DISTANCE_MM = 300
SQUARE_SIDE_MM = 250
PAUSE_MS = 1000


hub = PrimeHub()

left_motor = Motor(LEFT_DRIVE_PORT, Direction.COUNTERCLOCKWISE)
right_motor = Motor(RIGHT_DRIVE_PORT, Direction.CLOCKWISE)

robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=WHEEL_DIAMETER_MM,
    axle_track=AXLE_TRACK_MM,
)

# Moderate speeds are easier and safer for a first physical test.
robot.settings(
    straight_speed=250,
    straight_acceleration=500,
    turn_rate=120,
    turn_acceleration=240,
)

# Use the Prime Hub gyro to improve straight driving and turns.
# Change to False if you want to test motor-encoder control only.
robot.use_gyro(True)


def announce(message):
    """Print a test label and give a short audible signal."""
    print(message)
    hub.speaker.beep(600, 100)
    wait(300)


def test_straight_back_and_forth(distance_mm=STRAIGHT_DISTANCE_MM):
    """Drive forward by distance_mm, then reverse to the start."""
    announce("Straight test: forward")
    robot.straight(distance_mm)
    wait(PAUSE_MS)

    announce("Straight test: backward")
    robot.straight(-distance_mm)
    wait(PAUSE_MS)


def drive_square(side_mm=SQUARE_SIDE_MM, turn_angle=90):
    """Drive a four-sided square.

    Pybricks uses positive angles for right/clockwise turns and negative
    angles for left/counterclockwise turns.
    """
    direction_name = "right" if turn_angle > 0 else "left"
    announce("Square test: " + direction_name + " turns")

    for side_number in range(1, 5):
        print("Side", side_number)
        robot.straight(side_mm)
        robot.turn(turn_angle)

    wait(PAUSE_MS)


def main():
    hub.light.on(Color.ORANGE)

    test_straight_back_and_forth()
    drive_square(turn_angle=90)   # Four right turns.
    drive_square(turn_angle=-90)  # Four left turns.

    robot.stop()
    hub.light.on(Color.GREEN)
    hub.speaker.beep(880, 250)
    print("All base robot tests completed.")


if __name__ == "__main__":
    main()
