"""Export the route saved by run2 as CSV over USB.

Run from the computer with:

    python -m pybricksdev run usb hardware/export_route.py

Redirect the CSV output to a file if desired.
"""

from pybricks.hubs import PrimeHub

from run2 import read_sample, saved_sample_count


hub = PrimeHub()
sample_count = saved_sample_count(hub)

print("sample,time_ms,left_angle,right_angle,left_speed,right_speed,heading")
for sample_number in range(sample_count):
    sample = read_sample(hub, sample_number)
    print(
        sample_number,
        sample[0],
        sample[1],
        sample[2],
        sample[3],
        sample[4],
        sample[5],
        sep=",",
    )
