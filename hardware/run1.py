"""Physical robot movement tests."""

from pybricks.tools import wait


STRAIGHT_DISTANCE_MM = 300
SQUARE_SIDE_MM = 250
CURVE_RADIUS_MM = 128
CURVE_ANGLE_DEG = 180
PAUSE_MS = 1000


async def announce(hub, message):
    """Print a test label and give a short audible signal."""
    print(message)
    await hub.speaker.beep(600, 100)
    await wait(300)


async def test_straight_back_and_forth(hub, robot, distance_mm=STRAIGHT_DISTANCE_MM):
    """Drive forward by distance_mm, then reverse to the start."""
    await announce(hub, "Straight test: forward")
    await robot.straight(distance_mm)
    await wait(PAUSE_MS)

    await announce(hub, "Straight test: backward")
    await robot.straight(-distance_mm)
    await wait(PAUSE_MS)


async def drive_square(hub, robot, side_mm=SQUARE_SIDE_MM, turn_angle=90):
    """Drive a four-sided square."""
    direction_name = "right" if turn_angle > 0 else "left"
    await announce(hub, "Square test: " + direction_name + " turns")

    for side_number in range(1, 5):
        print("Side", side_number)
        await robot.straight(side_mm)
        await robot.turn(turn_angle)

    await wait(PAUSE_MS)


async def curve_test(hub, robot, radius_mm=CURVE_RADIUS_MM, angle_deg=CURVE_ANGLE_DEG):
    """Drive a half-circle to the right, then a half-circle to the left."""
    await announce(hub, "Curve test: right")
    await robot.arc(radius_mm, angle=angle_deg)
    await wait(PAUSE_MS)

    await announce(hub, "Curve test: left")
    await robot.arc(-radius_mm, angle=angle_deg)
    await wait(PAUSE_MS)


async def run1(hub, robot, left_motor, right_motor):
    """Run the base robot movement tests."""
    await test_straight_back_and_forth(hub, robot)
    await drive_square(hub, robot, turn_angle=90)
    await drive_square(hub, robot, turn_angle=-90)
    await curve_test(hub, robot)
    print("All base robot tests completed.")