# Gears Setup and Pybricks Compatibility

## 1. Open the simulator

Use either:

- hosted stable site: <https://gears.aposteriori.com.sg/>
- project build: <https://quirkycort.github.io/gears/public/>

For a local offline copy, download the Gears repository, change into its `public` directory, and run:

```console
python -m http.server 1337 --bind 127.0.0.1
```

Then open <http://127.0.0.1:1337>. A web server is required; opening `index.html` directly can fail because of browser CORS rules.

## 2. Configure the standard course robot

1. Open the robot menu and select **Double Sensor Line Follower** (`doubleFollower`).
2. Open the world menu. Use **Grid** for Weeks 1–3, **Line Following** for Weeks 4–6, **Missions/FLL 2024** for Weeks 7–12, and the named challenge world when a lesson specifies one.
3. Switch the programming language to **Pybricks**.
4. Switch to the **Python** editor.
5. Load `starter_code/gears/main.py`, or load the whole starter folder as a zip for multi-module work.
6. Press Run. Stop before changing the robot or world.

The standard robot exposes:

| Device | Gears port | Course name | Physical SPIKE example |
|---|---:|---|---|
| Left drive motor | A | `r.left_motor` | C |
| Right drive motor | B | `r.right_motor` | D |
| Attachment actuator | C | `r.attachment_motor` | E or F |
| Left color sensor | S1 | `r.left_color` | A |
| Right color sensor | S2 | `r.right_color` | B |
| Ultrasonic sensor | S3 | `r.distance_sensor` | optional distance sensor |
| Gyro sensor | S4 | `r.gyro` | built into PrimeHub |

The port difference is intentional: mission logic refers to named attributes, so only `robot.py` changes during a hardware port.

## 3. Compatibility boundary

Do not tell students that Gears is a full SPIKE Prime emulator. It is a general educational robotics simulator with early Pybricks support.

| Concept | Current Pybricks | Gears course support | Teaching decision |
|---|---|---|---|
| Device imports | `pybricks.pupdevices` | `pybricks.ev3devices` | hidden in `robot.py` |
| Hub | `PrimeHub` | `EV3Brick` | avoid hub-display menu in simulator |
| `DriveBase.straight()` | yes; async-capable in current docs | yes; synchronous | use directly |
| `DriveBase.turn()` | relative or absolute in current docs | relative only | use relative turns |
| `DriveBase.arc()` | yes | not implemented | approximate with `drive()` or split segments |
| `DriveBase.settings()` | yes | yes, positional values | use four explicit arguments |
| `drive()`, `stop()` | yes | yes | use for sensor control loops |
| distance/angle/state/reset | yes | yes, reduced reset signature | use for measurement labs |
| `use_gyro()` | yes | not implemented | write a gyro feedback helper |
| `done()`, `stalled()` | yes | not implemented | use explicit state/sensor/time limits |
| stop mode on `straight/turn` | supported | not accepted | omit `then=` in simulator calls |
| `await` | shown for supported current firmware/API modes | simulator calls are synchronous | add `await` only during hardware port if required by chosen firmware/API mode |

## 4. Saving student work

At the end of every session:

1. Stop the program.
2. Save Python to the computer.
3. Name the file or zip `team##_w##_v##`.
4. Record the world, robot, start pose, constants, result, and next change in the engineering log.

Gears can load a zip containing `main.py` and additional Python modules. This is the preferred format from Week 8 onward.

## 5. Instructor smoke test

Run this before Week 1:

```python
from pybricks.parameters import Port
from pybricks.ev3devices import Motor
from pybricks.robotics import DriveBase

left = Motor(Port.A)
right = Motor(Port.B)
drive_base = DriveBase(left, right, 56, 152)
drive_base.straight(300)
drive_base.turn(90)
drive_base.straight(300)
```

Verify that the robot travels forward, turns right, and stops. If forward is reversed, use `Direction.COUNTERCLOCKWISE` on both motors or inspect the selected template.

## 6. Troubleshooting

- **Nothing moves:** confirm Pybricks mode, motor ports A/B, and that the program is running.
- **Robot spins during `straight`:** one drive motor direction is inverted.
- **Sensor value never changes:** confirm the selected robot actually has that sensor and the expected input port.
- **Browser freezes:** every sensor loop must call `wait(10)` or another short delay.
- **A multi-file zip does not load:** ensure its entry file is exactly `main.py` (or `gearsPython.py`).
- **Blocks disappeared:** Python edits do not round-trip back into Blockly. Save before switching modes.
- **FLL 2025 has no working model:** use the bundled FLL 2024 world for interactive capstone missions.

## 7. Hardware transfer checklist

When moving to SPIKE Prime:

1. Replace EV3-style imports with `PrimeHub`, `pupdevices`, and SPIKE ports.
2. Measure the physical wheel diameter and axle track; do not copy simulator values blindly.
3. Set hub orientation and motor positive directions.
4. Replace `GyroSensor` access with the hub IMU or `DriveBase.use_gyro(True)` as appropriate.
5. Re-check the current Pybricks call style for the firmware/API version in use, including whether a maneuver is awaited.
6. Test one helper at low speed, then one mission, before loading the full menu.
7. Recalibrate color thresholds and every distance/turn on the physical mat.
