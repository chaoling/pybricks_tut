# Instructor Guide

## Course shape

The course assumes two 90-minute sessions per week. Each meeting follows a predictable routine:

- 10 min — retrieval warm-up and goal
- 15 min — instructor model or code reading
- 45 min — paired build/test cycle
- 15 min — challenge run and evidence capture
- 5 min — engineering-log exit ticket

Teams of two work best. Rotate **driver** (operates simulator and types), **navigator** (reads plan and checks values), and, for groups of three, **test engineer** (records evidence) every 20 minutes.

## Mastery model

Students advance through four repeated levels:

1. **Make it move:** program executes without errors.
2. **Make it accurate:** endpoint or sensor condition is correct.
3. **Make it reusable:** code is named, parameterized, and modular.
4. **Make it reliable:** success is demonstrated across repeated trials and explained with data.

Do not award full challenge credit for a single lucky run. From Week 2 onward, require at least five trials; Weeks 9–12 require ten trials for reliability claims.

## Engineering log template

Each team keeps one log with this record for every meaningful test:

| Field | Entry |
|---|---|
| Date / programmer / reviewer | |
| World and start pose | |
| Goal and success tolerance | |
| Code version | |
| Constants changed | |
| Predicted result | |
| Actual result | |
| Evidence (time, endpoint, sensor value, success) | |
| One-variable next change | |
| Why that change should help | |

Teach students to change one variable at a time. A test without a recorded start condition is not reproducible evidence.

## Common misconceptions to address

- A positive Pybricks turn is right/clockwise when viewed from above; negative is left/counterclockwise.
- Wheel diameter affects distance scaling; axle track affects turn scaling.
- Encoder distance is an estimate, not a global position measurement.
- Higher speed usually reduces margin for correction and attachment contact.
- `wait()` is not a precision navigation strategy; it is primarily a scheduler-friendly delay in sensor loops.
- A color threshold is the midpoint between measured light and dark values, not a universal magic number.
- Proportional gain is not “accuracy.” It determines how strongly error changes steering.
- A simulator removes many physical variations. Reliability still needs deliberate perturbation tests.

## Differentiation

For students who need support:

- provide partially completed functions with one missing expression;
- require a flowchart before code;
- use only one color sensor for the first line-following lab;
- give a table of test values and ask students to predict before running;
- score a smaller route with the same reliability expectations.

For students ready to extend:

- implement a PD rather than P controller;
- create a generic `drive_until(predicate, timeout_ms)` helper;
- compare encoder and gyro heading estimates;
- add a mission registry rather than an `if/elif` dispatcher;
- perturb friction, starting angle, or starting position and graph success rate;
- design and share a custom Gears mission world.

## Safety and competition habits

Even in a virtual class, rehearse physical-robot habits: announce before running, keep hands clear of mechanisms, stop before touching the robot, begin at controlled speed, inspect attachments, and never rely on a stall indefinitely. These habits transfer directly to the team table.

## Weekly preparation

| Week | Instructor preparation |
|---:|---|
| 1 | Smoke-test Gears and starter code; reset Grid world |
| 2 | Prepare endpoint tolerance markers and trial sheet |
| 3 | Prepare two route cards with distances and headings |
| 4 | Verify color-stop and ultrasonic challenge worlds |
| 5 | Verify simple, sharp, gap, and obstacle line worlds |
| 6 | Verify Gyro Straight and Gyro Square worlds |
| 7 | Verify attachment actuator on port C; select two FLL objects |
| 8 | Test multi-module zip loading; distribute architecture diagram |
| 9 | Publish mission acceptance criteria and home boundary |
| 10 | Prepare route-combination score sheet and 150-second timer |
| 11 | Prepare perturbation cards and reliability board |
| 12 | Run two mock tables; print capstone rubric |

## Evidence portfolio

Every student portfolio should contain:

- Week 2 calibration/repeatability table;
- Week 5 line-following controller and tuning evidence;
- Week 6 gyro controller and comparison data;
- Week 8 multi-module code archive;
- Week 11 reliability report;
- Week 12 capstone archive, match score sheet, and SPIKE transfer reflection.

## Source-informed teaching notes

Current Pybricks documentation emphasizes measured robot dimensions, explicit speed/acceleration settings, relative versus absolute heading, continuous drive for sensor-triggered motion, and calibration by long straight and full-turn tests. Those practices are threaded through the course. The SPIYKE reference architecture is introduced only after students understand the primitives, so modules solve an organizational problem students have already experienced.
