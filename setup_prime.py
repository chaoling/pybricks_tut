from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
# Go through all the colors.
for hue in range(360):
    hub.light.on(Color(hue))
    wait(10)

left = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right = Motor(Port.F, Direction.CLOCKWISE)
right_mm = Motor(Port.B)
left_mm = Motor(Port.C)
robot = DriveBase(left, right, wheel_diameter=56, axle_track=128)

# The main program starts here.
# Make both motors perform an action with wait=False aka running in parallel
right_mm.run_angle(500, 360, then=Stop.HOLD, wait=False)
left_mm.run_angle(500, 720, then=Stop.HOLD, wait=False)
# While one or both of the motors are not done yet,
# do something else. In this example, just wait.
while not right_mm.done() or not left_mm.done():
    wait(1)

print("Both motors are done!")

# Curved turns:
robot.curve(radius=128,angle=180, then=Stop.HOLD, wait=True)
# Drive in a square.
for count in range(4):
    robot.straight(250)
    right_mm.run_target(500, count*90, then=Stop.HOLD, wait=False)
    left_mm.run_target(500, -90*count, then=Stop.HOLD, wait=False)
    robot.turn(90)