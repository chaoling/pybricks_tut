"""Reusable pre-run gyro readiness check for a SPIKE Prime DriveBase.

Copy ``prepare_gyro_for_run`` into the team's base code, or import this module.
The persistent heading correction is created separately by
``spike_prime_gyro_heading_calibration.py`` and should not be re-measured before
every mission.
"""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Color, Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait


LEFT_DRIVE_PORT = Port.D
RIGHT_DRIVE_PORT = Port.F
WHEEL_DIAMETER_MM = 56
AXLE_TRACK_MM = 100


def prepare_gyro_for_run(hub, drive_base):
    """Wait for automatic bias calibration, enable gyro control, and zero yaw."""
    drive_base.use_gyro(False)
    hub.light.on(Color.ORANGE)
    hub.display.char("S")
    print("Do not touch the robot. Waiting for IMU calibration...")

    while not (hub.imu.stationary() and hub.imu.ready()):
        wait(50)

    # Enable gyro feedback only after calibration, then establish the mission's
    # current physical orientation as absolute heading zero.
    drive_base.use_gyro(True)
    drive_base.reset(distance=0, angle=0)

    hub.light.on(Color.GREEN)
    hub.display.char("R")
    hub.speaker.beep(880, 150)
    print("Gyro ready. Heading:", drive_base.angle())


def main():
    # This demonstration hardware is constructed only when this file is run
    # directly. Importing prepare_gyro_for_run() will not claim any hub ports.
    hub = PrimeHub()
    left_motor = Motor(LEFT_DRIVE_PORT, Direction.COUNTERCLOCKWISE)
    right_motor = Motor(RIGHT_DRIVE_PORT, Direction.CLOCKWISE)

    robot = DriveBase(
        left_motor,
        right_motor,
        wheel_diameter=WHEEL_DIAMETER_MM,
        axle_track=AXLE_TRACK_MM,
    )

    prepare_gyro_for_run(hub, robot)

    # Replace this demonstration with the actual FLL mission.
    robot.straight(300)
    robot.turn(90)
    robot.straight(300)
    robot.turn(-90)

    robot.stop()
    hub.light.on(Color.GREEN)
    print("Startup demonstration complete.")


if __name__ == "__main__":
    main()
