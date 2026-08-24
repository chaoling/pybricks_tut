---
layout: home
title: FLL Pybricks Virtual Robotics
---

# Master FLL robot programming in 12 weeks

This free, simulator-first course teaches students to design, program, test, and explain reliable FLL-level autonomous robot missions using Python, Pybricks concepts, and the [Gears virtual robotics environment](https://gears.aposteriori.com.sg/).

The default schedule is two 90-minute meetings per week for grades 6–9. Students progress from their first precise movement to closed-loop control, modular competition code, reliability engineering, and a 150-second mock match.

## Course materials

- [Complete 12-week curriculum]({{ '/course/CURRICULUM.html' | relative_url }})
- [Gears setup and Pybricks compatibility]({{ '/course/GEARS_SETUP.html' | relative_url }})
- [Instructor guide]({{ '/course/INSTRUCTOR_GUIDE.html' | relative_url }})
- [Assessment and capstone rubrics]({{ '/course/ASSESSMENT.html' | relative_url }})
- [Printable engineering log]({{ '/student_templates/ENGINEERING_LOG.html' | relative_url }})
- [Printable mission design sheet]({{ '/student_templates/MISSION_DESIGN.html' | relative_url }})
- [Gears starter-code folder](https://github.com/chaoling/pybricks_tut/tree/main/starter_code/gears)

## Learning progression

| Week | Focus | Student outcome |
|---:|---|---|
| 1 | Commands and coordinates | Complete a measured autonomous route |
| 2 | Geometry and calibration | Collect and interpret repeatability data |
| 3 | Functions and loops | Build a reusable route library |
| 4 | Sensors and conditions | Create bounded sensor-triggered behaviors |
| 5 | Proportional control | Tune a line-following controller |
| 6 | Gyro feedback | Hold and measure robot heading |
| 7 | Attachments | Coordinate mechanism and drive actions |
| 8 | Modules and interfaces | Build a SPIYKE-style mission codebase |
| 9 | Mission decomposition | Complete reliable FLL-style objectives |
| 10 | Match strategy | Optimize a 150-second route plan |
| 11 | Reliability engineering | Complete a controlled ten-trial review |
| 12 | Capstone | Run, defend, and port the complete system |

## What students master

- Python sequences, variables, loops, conditions, functions, and modules
- accurate straight, turn, speed, and attachment-motor movements
- reflected-light, gyro, distance, and encoder feedback
- proportional line and heading control
- calibration, repeatability testing, and failure analysis
- modular mission architecture and match strategy
- deliberate transfer from Gears to a physical SPIKE Prime robot

## Technical foundation

The course is based on the [official Pybricks robotics documentation](https://docs.pybricks.com/en/latest/robotics.html), the mission-oriented structure of [fssfll/spike_basecode](https://github.com/fssfll/spike_basecode), and the [Gears simulator](https://github.com/QuirkyCort/gears).

Gears implements an older, synchronous Pybricks subset rather than a complete SPIKE Prime emulator. The course labels those differences explicitly and ends with a hardware-transfer checklist so students understand what must be reconfigured and recalibrated on a real robot.

## License and reuse

The course links to but does not redistribute Pybricks, Gears, or SPIYKE source code. Course materials may be adapted for educational use; check upstream licenses before redistributing upstream assets.
