"""Gears entry point.

Change MISSION_NUMBER to choose a mission. A physical SPIKE version can replace
this dispatcher with the hub menu pattern used by fssfll/spike_basecode.
"""

from robot import Robot
from mission_01 import mission_01

try:
    from mission_02 import mission_02
except ImportError:
    mission_02 = None

try:
    from mission_03 import mission_03
except ImportError:
    mission_03 = None

try:
    from mission_04 import mission_04
except ImportError:
    mission_04 = None


MISSION_NUMBER = 1


def main():
    r = Robot()
    try:
        if MISSION_NUMBER == 1:
            mission_01(r)
        elif MISSION_NUMBER == 2:
            if mission_02 is None:
                print("Mission 2 is not implemented yet.")
            else:
                mission_02(r)
        elif MISSION_NUMBER == 3:
            if mission_03 is None:
                print("Mission 3 is not implemented yet.")
            else:
                mission_03(r)
        elif MISSION_NUMBER == 4:
            if mission_04 is None:
                print("Mission 4 is not implemented yet.")
            else:
                mission_04(r)
        else:
            print("Unknown mission:", MISSION_NUMBER)
    finally:
        r.stop_all()


if __name__ == "__main__":
    main()
