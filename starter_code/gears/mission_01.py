"""Example mission: leave home, operate an attachment, and return."""

from pybricks.parameters import Stop
from robot import Robot


def mission_01(r):
    # Distances are millimeters; positive turns are clockwise/right.
    r.drive_base.straight(450)
    r.drive_base.turn(45)

    # Start the attachment and continue immediately.
    r.attachment_motor.run_angle(500, 180, then=Stop.HOLD, wait=False)
    r.drive_base.straight(250)

    r.drive_base.straight(-250)
    r.drive_base.turn(-45)
    r.drive_base.straight(-450)


if __name__ == "__main__":
    mission_01(Robot())
