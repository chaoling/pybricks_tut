"""Example mission: leave home, operate an attachment, and return."""

from pybricks.parameters import Stop
from robot import Robot


def mission_02(r):
    # Distances are millimeters; positive turns are clockwise/right.
    r.drive_base.straight(550)
    r.drive_base.turn(145)

    # Start the attachment and continue immediately.
    r.attachment_motor.run_angle(500, 180, then=Stop.HOLD, wait=False)
    r.drive_base.straight(550)

    r.drive_base.straight(-550)
    r.drive_base.turn(-145)
    r.drive_base.straight(-550)


if __name__ == "__main__":
    mission_02(Robot())