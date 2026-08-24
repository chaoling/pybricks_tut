"""Gears entry point.

Change MISSION_NUMBER to choose a mission. A physical SPIKE version can replace
this dispatcher with the hub menu pattern used by fssfll/spike_basecode.
"""

from robot import Robot
from mission_01 import mission_01


MISSION_NUMBER = 1


def main():
    r = Robot()
    try:
        if MISSION_NUMBER == 1:
            mission_01(r)
        else:
            print("Unknown mission:", MISSION_NUMBER)
    finally:
        r.stop_all()


if __name__ == "__main__":
    main()
