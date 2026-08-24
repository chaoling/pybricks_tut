"""Copy this file, rename it, and keep the public mission function small."""


APPROACH_DISTANCE_MM = 300
APPROACH_SPEED_MM_S = 180


def approach(r):
    """Navigate from the mission's known launch pose to its alignment area."""
    r.drive_base.settings(APPROACH_SPEED_MM_S, 500, 120, 240)
    r.drive_base.straight(APPROACH_DISTANCE_MM)


def operate(r):
    """Change the target model's observable state."""
    # Replace with a bounded attachment action.
    pass


def return_home(r):
    """Return from the known post-operation pose."""
    r.drive_base.straight(-APPROACH_DISTANCE_MM)


def mission_template(r):
    """Top-level plan: approach, operate, and return safely."""
    approach(r)
    operate(r)
    return_home(r)
