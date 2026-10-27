"""Course robot adapter for the Gears doubleFollower robot.

Mission files use names such as ``r.drive_base`` and ``r.left_color``.
Only this file should need a major rewrite when moving to SPIKE Prime.
"""

from pybricks.ev3devices import ColorSensor, GyroSensor, Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait


WHEEL_DIAMETER_MM = 56
AXLE_TRACK_MM = 152
STRAIGHT_SPEED_MM_S = 300
STRAIGHT_ACCEL_MM_S2 = 600
TURN_RATE_DEG_S = 180
TURN_ACCEL_DEG_S2 = 360


class Robot:
    """Named access to the standard virtual robot's devices."""

    def __init__(self):
        self.left_motor = Motor(Port.A)
        self.right_motor = Motor(Port.B)
        self.attachment_motor = Motor(Port.C)

        self.left_color = ColorSensor(Port.S1)
        self.right_color = ColorSensor(Port.S2)
        self.distance_sensor = UltrasonicSensor(Port.S3)
        self.gyro = GyroSensor(Port.S4)

        self.drive_base = DriveBase(
            self.left_motor,
            self.right_motor,
            WHEEL_DIAMETER_MM,
            AXLE_TRACK_MM,
        )
        self.drive_base.settings(
            STRAIGHT_SPEED_MM_S,
            STRAIGHT_ACCEL_MM_S2,
            TURN_RATE_DEG_S,
            TURN_ACCEL_DEG_S2,
        )

        # Familiar alias for teams adapting SPIYKE-style mission examples.
        self.robot = self.drive_base

    def stop_all(self):
        self.drive_base.stop()
        self.attachment_motor.stop()

    def drive_until_dark(self, speed_mm_s=150, threshold=35, limit_mm=600):
        """Drive until the left sensor sees dark or the limit is reached."""
        self.drive_base.reset()
        self.drive_base.drive(speed_mm_s, 0)
        while (
            self.left_color.reflection() > threshold
            and abs(self.drive_base.distance()) < limit_mm
        ):
            wait(10)
        self.drive_base.stop()

    def gyro_straight(self, distance_mm, speed_mm_s=200, kp=2.0):
        """Hold the starting gyro heading with proportional correction.

        If the robot corrects in the wrong direction for the selected Gears
        template, negate ``correction`` and record why in the engineering log.
        """
        self.gyro.reset_angle(0)
        self.drive_base.reset()
        direction = 1 if distance_mm >= 0 else -1
        while abs(self.drive_base.distance()) < abs(distance_mm):
            error = 0 - self.gyro.angle()
            correction = kp * error
            self.drive_base.drive(direction * abs(speed_mm_s), correction)
            wait(10)
        self.drive_base.stop()


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

# Lower-case alias mirrors the class name used by the SPIYKE reference.
if __name__ == "__main__":
    r = Robot
    mission_01(r)