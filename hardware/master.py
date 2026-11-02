"""Physical SPIKE Prime master program.

Upload this file with its sibling modules. Add a run function to ``runs.py``
to make it available in the hub menu.
"""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import hub_menu, multitask, run_task, wait

from runs import RUNS


hub = PrimeHub()

LEFT_DRIVE_PORT = Port.D
RIGHT_DRIVE_PORT = Port.F
LEFT_DRIVE_DIRECTION = Direction.COUNTERCLOCKWISE
RIGHT_DRIVE_DIRECTION = Direction.CLOCKWISE
WHEEL_DIAMETER_MM = 56
AXLE_TRACK_MM = 128
STRAIGHT_SPEED_MM_S = 250
STRAIGHT_ACCEL_MM_S2 = 500
TURN_RATE_DEG_S = 120
TURN_ACCEL_DEG_S2 = 240

left_motor = Motor(LEFT_DRIVE_PORT, LEFT_DRIVE_DIRECTION)
right_motor = Motor(RIGHT_DRIVE_PORT, RIGHT_DRIVE_DIRECTION)
robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=WHEEL_DIAMETER_MM,
    axle_track=AXLE_TRACK_MM,
)
robot.settings(
    STRAIGHT_SPEED_MM_S,
    STRAIGHT_ACCEL_MM_S2,
    TURN_RATE_DEG_S,
    TURN_ACCEL_DEG_S2,
)
robot.use_gyro(True)


def choose_run():
    """Use the built-in hub menu to select a run from 1 through N."""
    if not RUNS:
        raise ValueError("Add at least one run to runs.py")

    run_number = hub_menu(*range(1, len(RUNS) + 1))
    return run_number, RUNS[run_number - 1]


async def emergency_stop():
    """Stop the robot when the hub Bluetooth button is pressed."""
    while True:
        if Button.BLUETOOTH in hub.buttons.pressed():
            robot.stop()
            hub.light.on(Color.RED)
            await hub.speaker.beep(220, 500)
            return True
        await wait(20)


async def main(run_number, run_program):
    """Run the selected program with an emergency-stop monitor."""
    hub.display.number(run_number)
    stopped = False
    try:
        _, stopped = await multitask(
            run_program(hub, robot, left_motor, right_motor),
            emergency_stop(),
            race=True,
        )
        if stopped:
            print("Emergency stop pressed.")
    finally:
        robot.stop()
        if not stopped:
            hub.light.on(Color.GREEN)
            hub.speaker.beep(880, 250)


if __name__ == "__main__":
    hub.light.on(Color.ORANGE)
    selected_run_number, selected_run = choose_run()
    run_task(main(selected_run_number, selected_run))