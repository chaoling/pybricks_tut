"""One-time SPIKE Prime gyro heading calibration for Pybricks.

Run this program when setting up a hub, after changing the robot build, or
after updating the Pybricks firmware. It measures the raw gyro result for a
physical 360-degree clockwise rotation and saves the average as the persistent
``heading_correction`` value.

This is a manual measurement, not a motor-driven turn. Put the robot on a
turntable or a paper angle guide, mark its initial direction, and return it to
that mark as accurately as possible. Perform all trials clockwise.

Controls:
    Center button: start/end each measurement
    Bluetooth button: stop the program

The hub must be mounted flat for the default PrimeHub orientation. If it is
mounted differently, provide the correct ``top_side`` and ``front_side``
arguments when constructing PrimeHub.
"""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Button, Color
from pybricks.tools import wait


# The documented defaults normally work in a quiet room. Increase them only
# if imu.stationary() never becomes True in the actual competition environment.
ANGULAR_VELOCITY_THRESHOLD = 2       # deg/s
ACCELERATION_THRESHOLD = 2500       # mm/s^2

CALIBRATION_TRIALS = 3
MIN_REASONABLE_ROTATION = 300        # deg
MAX_REASONABLE_ROTATION = 420        # deg
POLL_INTERVAL_MS = 20


hub = PrimeHub()


def beep(frequency=700, duration=100):
    """Give a short audible status signal."""
    hub.speaker.beep(frequency, duration)


def wait_for_center_press():
    """Wait for a new center-button press and release."""
    while Button.CENTER in hub.buttons.pressed():
        wait(POLL_INTERVAL_MS)

    while Button.CENTER not in hub.buttons.pressed():
        wait(POLL_INTERVAL_MS)

    while Button.CENTER in hub.buttons.pressed():
        wait(POLL_INTERVAL_MS)


def wait_until_imu_ready():
    """Keep the robot still until automatic gyro bias calibration completes."""
    print("Keep the robot completely still...")
    hub.display.char("S")
    hub.light.on(Color.ORANGE)

    while not (hub.imu.stationary() and hub.imu.ready()):
        wait(50)

    hub.display.char("R")
    hub.light.on(Color.GREEN)
    beep(880, 150)
    print("IMU is stationary and ready.")


def measure_one_full_turn(trial_number):
    """Measure one manually performed, physical clockwise 360-degree turn."""
    print("\nTrial", trial_number, "of", CALIBRATION_TRIALS)
    print("Align the robot with the start mark.")
    print("Press CENTER, rotate exactly 360 degrees clockwise, then press CENTER.")
    hub.display.number(trial_number)
    wait_for_center_press()

    # The documentation specifies -Axis.Z for a normal flat drive-base yaw
    # measurement. calibrated=False gives the raw value needed by
    # heading_correction.
    start_rotation = hub.imu.rotation(-Axis.Z, calibrated=False)
    hub.light.on(Color.BLUE)
    beep(660, 100)

    wait_for_center_press()
    end_rotation = hub.imu.rotation(-Axis.Z, calibrated=False)
    measured_rotation = abs(end_rotation - start_rotation)

    print("Raw rotation:", measured_rotation, "degrees")

    if not MIN_REASONABLE_ROTATION <= measured_rotation <= MAX_REASONABLE_ROTATION:
        hub.light.on(Color.RED)
        beep(220, 400)
        print("Measurement rejected. The robot did not appear to turn exactly once.")
        return None

    hub.light.on(Color.GREEN)
    beep(880, 100)
    return measured_rotation


def calibrate_heading():
    """Collect valid trials, average them, and save heading correction."""
    measurements = []

    while len(measurements) < CALIBRATION_TRIALS:
        measurement = measure_one_full_turn(len(measurements) + 1)
        if measurement is not None:
            measurements.append(measurement)

    heading_correction = sum(measurements) / len(measurements)

    print("\nMeasurements:", measurements)
    print("Average heading correction:", heading_correction)

    # Keyword arguments are intentional: the Pybricks documentation recommends
    # them so future additions to imu.settings() do not change the meaning.
    hub.imu.settings(heading_correction=heading_correction)

    print("Saved persistent IMU settings:")
    print(hub.imu.settings())

    hub.display.char("C")
    hub.light.on(Color.GREEN)
    beep(880, 150)
    wait(100)
    beep(1100, 250)


def main():
    # CENTER normally stops a Pybricks program. Use BLUETOOTH as the stop button
    # so CENTER can mark the beginning and end of a calibration trial.
    hub.system.set_stop_button(Button.BLUETOOTH)

    # These settings are persistent too. Setting them here makes the intended
    # calibration environment explicit without replacing bias/scale values.
    hub.imu.settings(
        angular_velocity_threshold=ANGULAR_VELOCITY_THRESHOLD,
        acceleration_threshold=ACCELERATION_THRESHOLD,
    )

    wait_until_imu_ready()
    calibrate_heading()

    print("Calibration complete. Restart or run the mission program.")


if __name__ == "__main__":
    main()
