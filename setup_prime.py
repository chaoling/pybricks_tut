
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right = Motor(Port.F, Direction.CLOCKWISE)
right_mm = Motor(Port.B)
left_mm = Motor(Port.C)
robot = DriveBase(left, right, 56, 128)
right_mm.run_target(500, 0, then=Stop.HOLD, wait=True)
left_mm.run_target(500, 0, then=Stop.HOLD, wait=True)
# The main program starts here.
# Drive in a square.
for count in range(4):
    robot.straight(250)
    right_mm.run_target(500, count*90, then=Stop.HOLD, wait=True)
    left_mm.run_target(500, -90*count, then=Stop.HOLD, wait=True)
    robot.turn(90)