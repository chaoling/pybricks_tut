"""Gears: compare S1 and S2 on the SAME surface.
Select SENSOR_PORT = Port.S1, sample black then white in separate runs.
Repeat with Port.S2. Place the selected sensor fully over the surface.
"""
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

SENSOR_PORT = Port.S1  # Change to Port.S2 for the right sensor
sensor = ColorSensor(SENSOR_PORT)
total = 0
for sample in range(5):
    reading = sensor.reflection()
    print(sample + 1, reading)
    total += reading
    wait(200)
print("Mean reflection:", total / 5)
