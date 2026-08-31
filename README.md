# FLL Pybricks Virtual Robotics — 12-Week Course

This repository contains a complete, simulator-first course for students to build FLL-level autonomous robot programming skills with Python. It uses the [Gears simulator](https://gears.aposteriori.com.sg/), the current [Pybricks robotics documentation](https://docs.pybricks.com/en/latest/robotics.html), and the mission-oriented structure of [fssfll/spike_basecode](https://github.com/fssfll/spike_basecode).

Published course website: <https://chaoling.github.io/pybricks_tut/>

The course is designed for grades 6–9, but it works for older beginners. The default schedule is two 90-minute meetings per week for 12 weeks (36 contact hours). A one-meeting-per-week version can combine the two sessions and assign the engineering-log work between meetings.

## Course outcomes

By the end, students can:

- write and debug readable Python using variables, loops, conditions, functions, and modules;
- command accurate distance, turn, speed, and attachment-motor movements;
- use reflected-light, gyro, and distance feedback in closed-loop behaviors;
- create and tune proportional line and heading controllers;
- calibrate a robot, collect repeatability data, and improve reliability systematically;
- organize code as a robot abstraction plus independent mission modules;
- plan, implement, test, and combine autonomous FLL-style mission runs;
- explain how their simulator code maps to a physical SPIKE Prime robot.

## Start here

1. Read [Instructor Guide](course/INSTRUCTOR_GUIDE.md).
2. Complete [Gears Setup and Compatibility](course/GEARS_SETUP.md) before the first class.
3. Teach from the [12-Week Curriculum](course/CURRICULUM.md).
4. Copy or zip the files in [starter_code/gears](starter_code/gears/) for student teams.
5. Score the capstone with [Assessment and Rubrics](course/ASSESSMENT.md).
6. Print or copy the [Engineering Log](student_templates/ENGINEERING_LOG.md) and [Mission Design Sheet](student_templates/MISSION_DESIGN.md).
7. For a physical robot, follow the [SPIKE Prime VS Code Setup Guide](hardware/Pybricks_SPIKE_Prime_VSCode_Setup_Guide.docx) and run the [base robot movement test](hardware/spike_prime_base_test.py).

The repository's pre-existing [setup_prime.py](setup_prime.py) is preserved as a physical SPIKE Prime experimentation script. It is not used by the Gears lessons: it has hardware-specific ports and should be checked against the current Pybricks API before running on a robot.

## Recommended Gears configuration

- Robot: **Double Sensor Line Follower** (`doubleFollower`)
- Drive motors: ports A and B
- Attachment actuator: port C
- Sensors: left color S1, right color S2, ultrasonic S3, gyro S4
- Wheel diameter: 56 mm
- Axle track: 152 mm
- Programming mode: Python → Pybricks

Gears also includes FLL mission worlds for multiple seasons. Use FLL 2024 for the capstone because that bundled world contains interactive objects; the bundled FLL 2025 world is primarily a mat image in the source snapshot reviewed for this course.

## Source basis and compatibility policy

The current Pybricks `DriveBase` documentation defines distance in millimeters, clockwise/right turns as positive, and supports `straight`, `turn`, `arc`, continuous `drive`, motion settings, state measurements, reset, and optional gyro-assisted control. Gears' bundled Pybricks layer supports a useful but smaller, older synchronous subset. Students use that shared subset during the virtual course and complete a deliberate hardware-porting exercise in Week 12.

The SPIYKE reference contributes the architecture: one robot configuration module, a small entry point, a mission selector, and one function per mission file. Its hub display menu is replaced in Gears by a `MISSION_NUMBER` constant because Gears simulates an EV3-style hub rather than the SPIKE Prime hub display.

Source review date: 2026-08-23.

## License note

This course links to but does not vendor Pybricks, Gears, or SPIYKE source code. Check each upstream project's license before redistributing upstream assets. Original course material and starter code in this repository may be adapted for educational use.
