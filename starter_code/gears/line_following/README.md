# Two-sensor line-following labs

Standalone Python samples for the Robot Pizza Delivery lesson. Open
[Gears](https://gears.aposteriori.com.sg/), select **Double Sensor Line Follower**,
choose **Line Following Challenges → Simple Curves**, and use the **Python /
Pybricks** editor.

Paste and run one sample at a time. These files do not use the parent folder's
`main.py` or `robot.py`. To load one as a project, save that sample as `main.py`.

## Robot configuration

| Device | Port |
|---|---|
| Left drive motor | A |
| Right drive motor | B |
| Left color sensor (`sensor1`) | S1 |
| Right color sensor (`sensor2`) | S2 |

The samples use a 56 mm wheel diameter and 152 mm axle track, matching the
course robot. Left and right refer to the robot facing forward.

## 1. Sensor Detective

Run `01_sensor_detective.py` with the selected sensor fully over black, then
over white. Change `SENSOR_PORT` from `Port.S1` to `Port.S2` and repeat. Record
the five readings and mean from each run: S1 black, S1 white, S2 black, S2 white.

Compare the sensors on the same surfaces. Raw subtraction assumes comparable
responses. This controller targets a difference of zero, so it does not need a
black/white midpoint threshold.

## 2. Delivery Bot

Start `02_delivery_bot.py` facing along the stripe, with the line centered
between the two sensors. Save the world, start x/y and heading so trials can be
repeated. Gears world position fields use centimeters; `DriveBase` uses
millimeters.

Begin with `MODE = "bang"` for fixed-size zigzag steering. Then change to
`MODE = "p"` for proportional steering:

```python
error = sensor1.reflection() - sensor2.reflection()
correction = KP * error
```

| Readings | Error | Expected steering |
|---|---|---|
| S1 darker than S2 | Negative | Left |
| Equal | Zero | Straight |
| S2 darker than S1 | Positive | Right |

Check the sign in a short run. If the robot turns away from the line, verify
sensor ports, subtraction order and forward motor motion before tuning gain.

At a fixed speed of 100 mm/s, try `KP` values of 0.5, 1, 2 and 3. Then hold your
preferred gain fixed and try speeds of 80, 120 and 160 mm/s. These are teaching
candidates, not guaranteed working settings. Record failed runs and repeat
the finalists.

## Trial limits and interpretation

- Steering is clamped to ±120 deg/s.
- Every control-loop iteration includes `wait(10)`.
- The program stops at 1200 mm of odometer travel or 20 seconds, whichever
  comes first. `finally` calls `base.stop()` on normal exits and Python errors.
- Stop manually if the robot is clearly lost. Odometer travel does not prove
  the robot followed the line or reached a finish marker.
- Equal readings are ambiguous. Both-white can mean a centered narrow line,
  a gap or a departure. Both-black can occur at a broad stripe or intersection.
  Sensor spacing relative to stripe width affects sensitivity. The sample
  does not implement recovery or junction decisions.

Use an overhead view to judge tracking. For the lesson challenge, a successful
trial reaches the distance limit within 20 seconds, keeps the line between the
sensors with no departure longer than one continuous second, and stops
automatically. Repeat five times from the same start.

## Compatibility

These examples use Gears' EV3-style Pybricks imports. Physical SPIKE Prime
requires different imports and ports, measured dimensions and fresh sensor
calibration. See the [course setup guide](../../../course/GEARS_SETUP.md).

The control logic has been checked with mocked devices for both steering
directions, equal readings, turn clamping and distance/time/error exits.
Complete a preflight in the hosted simulator before class; these checks do
not demonstrate completion of a simulated route.
