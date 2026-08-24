# 12-Week FLL Pybricks Virtual Robotics Curriculum

## Course at a glance

| Week | Programming focus | Robot skill | Required evidence |
|---:|---|---|---|
| 1 | sequence, calls, arguments | straight and turn | measured route |
| 2 | variables, calculations | geometry and calibration | five-trial table |
| 3 | loops and functions | paths and reusable moves | route library |
| 4 | conditions and bounded loops | sensor-triggered movement | three sensor challenges |
| 5 | proportional control | line following | tuning graph/table |
| 6 | feedback and state | gyro-straight and heading | controller checkpoint |
| 7 | nonblocking motor action | attachments and coordination | scored object mission |
| 8 | modules and interfaces | SPIYKE-style architecture | multi-file archive |
| 9 | decomposition and alignment | FLL mission runs | two reliable missions |
| 10 | optimization and timing | route combinations | 150-second plan |
| 11 | data and fault analysis | reliability engineering | ten-trial review |
| 12 | integration and defense | mock match and hardware port | final capstone |

The named worlds refer to worlds bundled with Gears. If a hosted version uses slightly different menu labels, choose the world whose name contains the words shown below.

---

## Week 1 — Coordinates, Commands, and the First Autonomous Route

### Essential question

How does a line of Python become a predictable robot movement?

### Targets

Students can:

- run, stop, edit, and save a Gears Python program;
- explain function call, object, method, argument, and unit;
- use `straight(distance)` and `turn(angle)` with correct signs;
- trace a sequential program before running it;
- distinguish syntax, runtime, and behavior errors.

### Setup

Robot: `doubleFollower`. World: Grid. Begin with only `main.py`; introduce the adapter as provided infrastructure, not as code students must understand yet.

### Session A — Simulator flight school

1. Demonstrate reset, camera views, sensor panel, Python/Pybricks mode, Run, and Stop.
2. Read this call aloud: `r.drive_base.straight(300)` means “ask this drive-base object to move its center about 300 mm forward.”
3. Establish signs: positive distance is forward; negative is backward; positive turn is right/clockwise; negative is left/counterclockwise.
4. Students predict and run: forward 300, right 90, backward 150, left 45.
5. Intentionally cause and classify three errors: missing parenthesis, misspelled method, wrong-sign behavior.

### Session B — Courier route

Teams create a route from home to three grid checkpoints and back. Requirements:

- at least four straight segments and three turns;
- at least one negative distance and one negative angle;
- a comment naming each checkpoint;
- final center position within one grid square and final heading within 15° of the planned pose.

Before running, the navigator draws a pose table:

| Step | Command | Predicted x/y region | Predicted heading |
|---:|---|---|---:|
| 1 | | | |

### Skill check

Given a new three-command route, individually write the code and circle every argument with its unit. Score with the weekly 0–4 scale.

### Exit ticket

Explain why `turn(-90)` does not mean “drive backward.”

### Extension

Write `return_to_start()` for a known out-and-back path without copying the outward commands unchanged.

---

## Week 2 — Robot Geometry, Calibration, and Repeatability

### Essential question

Why can mathematically correct code still miss its target?

### Targets

Students can:

- connect wheel rotation, circumference, and linear distance;
- explain why `wheel_diameter` scales straight motion and `axle_track` scales turning;
- set speed and acceleration with `DriveBase.settings()`;
- calculate mean, range, absolute error, and success rate;
- change one calibration variable at a time.

### Session A — Long-straight calibration

1. Inspect `WHEEL_DIAMETER_MM` and `AXLE_TRACK_MM` in `robot.py`.
2. Predict the result of a wrong wheel diameter that is too small.
3. Run `straight(1000)` five times from an identical pose. Record endpoint error.
4. Change only wheel diameter by a deliberately large amount, repeat, and explain the direction of error.
5. Restore 56 mm. Discuss why simulator-perfect values are still a model, not proof about a physical tire under load.

Trial table:

| Trial | Commanded mm | Actual/observed mm | Signed error | Absolute error | Success? |
|---:|---:|---:|---:|---:|---|

### Session B — Full-turn calibration and speed tradeoff

1. Run `turn(360)` with axle track 152 mm, then with a deliberately wrong value.
2. Use the Pybricks rule: if a physical robot turns too little, increase axle track; if it turns too far, decrease it. Explain why the simulator may behave more ideally.
3. Compare a 600 mm out-and-back route at low, medium, and high speed/acceleration settings.
4. Decide which settings give the best balance of time and endpoint consistency.

Use all four positional settings in Gears:

```python
r.drive_base.settings(300, 600, 180, 360)
```

### Skill check

Students receive two symptoms (“distance is 4% short,” “turn is 8° too far”) and name which constant to adjust and in which direction. Require reasoning, not only the answer.

### Required portfolio evidence

Five-trial table, calculations, chosen settings, and a one-paragraph limitation of simulator calibration.

### Extension

Calculate a proposed corrected wheel diameter using proportional reasoning, test it, and report whether the model held.

---

## Week 3 — Functions, Loops, and Path Planning

### Essential question

How can we express a long route without producing fragile copy-and-paste code?

### Targets

Students can:

- create a function with parameters;
- use a `for` loop for repeated geometry;
- use constants rather than unexplained numbers;
- decompose a route into named actions;
- choose between a pivot, segmented curve, and continuous steering approach.

### Session A — Shape laboratory

Students convert a copied square into a function:

```python
def regular_polygon(r, sides, side_mm):
    exterior_angle = 360 / sides
    for _ in range(sides):
        r.drive_base.straight(side_mm)
        r.drive_base.turn(exterior_angle)
```

Test triangle, square, pentagon, and hexagon. Discuss accumulated error and why the loop expresses the invariant structure.

Next, write `drive_rectangle(r, length_mm, width_mm)` and decide whether calling `regular_polygon` would make the code clearer or more confusing.

### Session B — Route library challenge

Teams receive one of two route cards and create at least three helpers:

- `leave_home(r, lane)`
- `approach_target(r, offset_mm)`
- `return_home(r)`

Requirements:

- each helper has one clear job;
- parameters carry units in their names;
- a repeated structure uses a loop;
- top-level mission code reads like a plan, not a motor transcript;
- route succeeds in 4/5 trials.

Gears does not implement the current Pybricks `DriveBase.arc()` method. Demonstrate a coarse simulator curve with `drive(speed, turn_rate)` plus a bounded condition, but label it as a simulator workaround rather than an `arc()` substitute with identical precision.

### Skill check

Refactor a 12-line copied route into one loop and one parameterized function, then explain what should remain explicit at the mission level.

### Exit ticket

When can abstraction make competition code harder to debug?

### Extension

Write a helper that accepts a list of `(distance, turn)` route segments and executes them.

---

## Week 4 — Sensors, Conditions, and Safe Control Loops

### Essential question

How can a robot decide when to stop instead of guessing how long to drive?

### Targets

Students can:

- read reflected-light, ultrasonic-distance, gyro-angle, and drive-distance values;
- use `if`, `while`, comparison, and Boolean operators;
- create a loop with a primary condition and a safety limit;
- state why every sensor loop needs a short wait;
- choose the correct sensor for an observable event.

### Session A — Sensor stations

Rotate through three short stations:

1. **Color stop:** run the Gears color-stop challenge. Print or inspect reflection values over light and dark surfaces. Drive until dark.
2. **Distance stop:** approach a wall and stop 120 mm away using `distance_sensor.distance()`.
3. **Angle watcher:** rotate slowly with `drive(0, rate)` and stop at a gyro target.

Safe loop pattern:

```python
r.drive_base.reset()
r.drive_base.drive(150, 0)
while (
    r.left_color.reflection() > DARK_THRESHOLD
    and abs(r.drive_base.distance()) < MAX_TRAVEL_MM
):
    wait(10)
r.drive_base.stop()
```

Students identify the goal condition, failure condition, scheduler delay, and cleanup action.

### Session B — Sensor triathlon

Complete all three without changing worlds during an attempt:

- stop on a dark line without crossing it by more than one robot length;
- approach an object and stop in the 100–140 mm band;
- turn to 90° using gyro feedback within ±5°.

Each behavior must include a distance, angle, or elapsed-iteration escape condition. An unbounded `while` loop earns no safety credit even if it works.

### Skill check

Given four failure stories, students choose encoder, color, gyro, or ultrasonic feedback and justify the choice.

### Exit ticket

What should the robot do if the expected line or object is missing?

### Extension

Write one generic `drive_until` helper with a timeout expressed in loop iterations.

---

## Week 5 — Line Following and Proportional Control

### Essential question

How can continuous error become continuous steering correction?

### Targets

Students can:

- calibrate black and white reflection values;
- compute a target midpoint and signed error;
- explain bang-bang versus proportional control;
- tune speed and proportional gain separately;
- prevent an infinite line-following run.

### Session A — From zigzag to proportional steering

1. Measure at least five reflection readings on black and five on white.
2. Compute `TARGET = (BLACK + WHITE) / 2`.
3. Implement bang-bang control and observe oscillation.
4. Replace it with proportional control:

```python
TARGET = 45
KP = 2.0
SPEED_MM_S = 140
MAX_DISTANCE_MM = 1500

r.drive_base.reset()
while abs(r.drive_base.distance()) < MAX_DISTANCE_MM:
    reflection = r.left_color.reflection()
    error = TARGET - reflection
    correction = KP * error
    r.drive_base.drive(SPEED_MM_S, correction)
    wait(10)
r.drive_base.stop()
```

If correction drives away from the edge, reverse the error or correction sign. Students must explain which sign convention their selected sensor/edge requires.

### Session B — Scientific tuning ladder

Use Line Following — Simple, then Sharp. Keep speed fixed and test at least four `KP` values. Then keep the best `KP` fixed and test three speeds.

| Trial | World | Speed | KP | Completion? | Time | Leaves line | Observation |
|---:|---|---:|---:|---|---:|---:|---|

Teams must make a data-backed choice. “It felt best” is not sufficient.

### Skill check

Draw the expected correction direction for readings below, at, and above the target. Predict the effect of very low and very high gain.

### Required portfolio evidence

Calibration readings, controller code, tuning table, and selected constants with reasoning.

### Extension

Add a derivative term based on change in error and compare maximum stable speed with the P controller.

---

## Week 6 — Gyro Heading Control and Robot State

### Essential question

How can feedback keep a robot on its intended heading while it moves?

### Targets

Students can:

- distinguish encoder-estimated turn angle from gyro heading;
- reset a reference heading deliberately;
- create and tune a proportional heading controller;
- inspect `distance()`, `angle()`, and `state()`;
- compare two navigation strategies with evidence.

### Session A — Heading-hold controller

Use Gyro — Straight. Start from the `gyro_straight` helper in `robot.py`, but require teams to trace every line and write the controller equation in words:

```text
heading error = target heading - measured heading
turn correction = proportional gain × heading error
```

Test the sign at low speed. Tune gain for a 1500 mm straight. Record lateral displacement and final gyro angle.

Discuss how current physical Pybricks can enable gyro use directly on `DriveBase`, while Gears lacks `use_gyro()` and therefore uses an explicit feedback loop.

### Session B — Gyro square and comparison

Run Gyro — Square with two methods:

- encoder-based `straight` plus `turn`;
- gyro-straight plus a gyro-bounded turn helper.

Complete five trials per method. Compare final heading, endpoint, time, and code complexity. Students must avoid claiming the gyro method is universally better if their data does not show it.

### Controller checkpoint

Submit calibration/baseline, controller code, loop safeguards, tuning evidence, performance trials, and oral explanation. Use the 60-point controller rubric.

### Exit ticket

When would resetting the gyro in the middle of a mission destroy useful information, and when would it help?

### Extension

Create `turn_to_heading(target_deg)` using an absolute gyro target, reduced speed near the target, tolerance, and maximum iteration count.

---

## Week 7 — Attachments and Coordinated Actions

### Essential question

How do we coordinate navigation and a mechanism without wasting match time?

### Targets

Students can:

- control an attachment by angle, time, and continuous speed;
- choose `COAST`, `BRAKE`, or `HOLD` intentionally;
- use `wait=False` for a safe overlapping action;
- separate approach, engage, verify, and retreat phases;
- add a bounded recovery action.

### Session A — Mechanism laboratory

In the FLL 2024 world, choose an object reachable with the port-C actuator. Test:

- `run_angle` for repeatable mechanism position;
- `run_time` for continuous action;
- `wait=False` to begin an attachment movement before driving;
- `HOLD` versus `COAST` after action.

Example coordination:

```python
r.attachment_motor.run_angle(500, 180, wait=False)
r.drive_base.straight(220)
r.drive_base.stop()
```

Students identify the collision/safety risk if the robot drives away before the mechanism is ready. Add a short approach segment or verification delay only where evidence shows it is needed.

### Session B — One-object scored mission

Mission phases:

1. launch repeatably from home;
2. navigate to a model;
3. operate the attachment;
4. withdraw without undoing the score;
5. return to home.

Requirements: named constants, at least two helper functions, attachment action coordinated with driving, and 4/5 successful runs.

### Skill check

Students annotate a timeline showing which motor actions block, overlap, and end.

### Exit ticket

When does `wait=False` improve a run, and when does it create a race condition?

### Extension

Create an attachment reset/home routine that avoids depending on a potentially unsupported stall detector in Gears.

---

## Week 8 — From Scripts to a Competition Codebase

### Essential question

What code structure lets several students build missions without breaking one another’s work?

### Targets

Students can:

- explain the responsibilities of entry point, robot configuration, dispatcher, and mission module;
- import and call functions across files;
- keep ports and geometry out of mission code;
- use a consistent mission function signature;
- load and save a multi-module Gears archive.

### Session A — Read the architecture

Compare the course starter with the SPIYKE pattern:

```text
main.py
  creates one Robot
  selects one mission
      |
robot.py ---------------- mission_01.py
ports, dimensions,        mission_01(r)
devices, shared helpers   uses named robot features
```

Read the SPIYKE ideas, not its hardware-specific lines: a centralized robot class, an entry point, a hub menu, and one mission function per file. Explain why Gears uses a constant dispatcher instead of `hub_menu`.

Teams convert Week 7 into:

- `robot.py`
- `main.py`
- `mission_01.py`
- `mission_02.py`

### Session B — Integration protocol

Each student owns one mission module. Integration rules:

- do not change port mappings in a mission;
- every mission accepts the same `r` object;
- shared helpers belong in `robot.py` only after two missions need them;
- constants local to one route stay in its mission file;
- every mission can be run directly for testing;
- `main.py` always stops devices in a `finally` block.

Swap archives with another team. The receiving team must select and run both missions without editing them. Record every unclear name or hidden assumption.

### Skill check

Students place ten example lines into the correct file and justify two borderline choices.

### Required portfolio evidence

A working zip with two mission modules, architecture diagram, and peer-maintainability notes.

### Extension

Replace the `if/elif` dispatcher with a mission dictionary and validate unsupported selections.

---

## Week 9 — FLL Mission Decomposition and Alignment

### Essential question

How do we turn a field objective into a reliable autonomous mission?

### Targets

Students can:

- define observable acceptance criteria before coding;
- choose launch and alignment references;
- split a mission into navigation, alignment, interaction, and return;
- combine encoder, line, gyro, wall, and model-contact strategies;
- classify failures by phase.

### Session A — Mission design review

Choose two interactive objectives in the bundled FLL 2024 world. For each, complete:

| Design question | Decision |
|---|---|
| What visible state earns success? | |
| What start pose can humans reproduce? | |
| What is the simplest path corridor? | |
| Which segment needs encoder distance? | |
| Where can a line, wall, or model reset error? | |
| What attachment action changes the model? | |
| What failure must trigger retreat? | |
| How will the robot return to home? | |

Students storyboard the route with no more than eight phases before coding.

### Session B — Two mission builds

Build two separate mission modules. For each mission:

- run five development trials;
- label failures as launch, navigation, alignment, contact, attachment, return, or code;
- fix the most frequent category first;
- demonstrate at least 4/5 success before combining anything.

Teach line squaring as an optional two-sensor technique: drive slowly until one sensor finds the line, stop or slow that side, and continue the other until both detect the reference. Include a maximum travel limit.

### Skill check

Teams conduct a two-minute design review: objective, observable success, route phases, riskiest assumption, and planned recovery.

### Exit ticket

Why is “the robot went to approximately the right place” not a mission acceptance criterion?

### Extension

Create a reusable two-sensor line-square helper and test its sensitivity to approach angle.

---

## Week 10 — Route Combination, Timing, and Match Strategy

### Essential question

When should reliable missions be combined, and when should they remain separate?

### Targets

Students can:

- calculate points or objectives per second and reliability-adjusted value;
- combine missions without creating hidden state dependencies;
- plan a 150-second match with buffer time;
- define abort and recovery decisions;
- preserve a known-good version before optimization.

### Session A — Route economics

Measure each mission’s median time and success rate. If the current practice world has no official scoring model, assign instructor-defined values based on difficulty.

Calculate:

```text
expected value = objective value × observed success rate
expected value per second = expected value ÷ median run time
```

Evaluate candidate pairs. Combining two missions saves launch/return time but may make a later objective inherit earlier position error.

### Session B — 150-second match plan

Teams create a schedule with:

- launch order;
- estimated time for each route;
- human reset time;
- at least 15 seconds of buffer;
- one route that can be dropped;
- one safe recovery if a mechanism misses;
- a code-freeze version and an experimental version.

Run three timed rehearsals. Do not count simulator reset/configuration time as match time, but do count every programmed run and team selection delay.

### Skill check

Given three routes with values, times, and success rates, students choose a match plan and defend it quantitatively.

### Exit ticket

What evidence would persuade you to split a combined run back into two launches?

### Extension

Use a list of route records to calculate the best schedule under 135 seconds, reserving 15 seconds as buffer.

---

## Week 11 — Reliability Engineering and Code Freeze

### Essential question

How do we know a robot program is ready for competition?

### Targets

Students can:

- run a controlled ten-trial test;
- introduce realistic perturbations deliberately;
- distinguish systematic error from random variation;
- use failure frequency and impact to prioritize work;
- freeze, label, and recover a known-good version.

### Session A — Reliability campaign

For every planned route, run ten unchanged trials. Record:

| Trial | Start offset/angle | Result | Time | Failure phase | Notes |
|---:|---|---|---:|---|---|

After baseline trials, draw two perturbation cards:

- starting position shifted by a small visible amount;
- starting heading offset by 2–5°;
- lower or higher route speed;
- different starting attachment angle;
- minor friction/world variation if the selected world supports it.

Do not randomize everything at once. The purpose is to discover sensitivity.

### Session B — Failure review and code freeze

Create a frequency/impact board. Fix only the highest-priority failure and rerun the relevant test. Accept a change only if evidence improves and no higher-value route regresses.

Freeze an archive named `team##_capstone_rc1.zip`. It must include the code, constants, mission list, known limitations, and successful world/robot configuration.

### Reliability review

Submit the ten-trial tables, perturbation results, failure classification, one evidence-based improvement, and honest readiness conclusion. Use the 60-point reliability rubric.

### Exit ticket

Why can a 9/10 route still be the wrong route for the first launch of a match?

### Extension

Compute a simple confidence interval or compare reliability-adjusted match plans with a small simulation.

---

## Week 12 — Mock Match, Technical Defense, and SPIKE Transfer

### Essential question

Can our team perform, explain, and transfer its autonomous system?

### Targets

Students can:

- operate a complete 150-second autonomous match plan;
- recover without unsafe or improvised code edits;
- explain control logic, architecture, testing, and strategy;
- identify every major change required for a physical SPIKE Prime;
- reflect on simulator benefits and limitations.

### Session A — Mock competition

Run two rounds with a short pit period.

Round procedure:

1. two-minute setup inspection;
2. 150-second match;
3. independent scoring against published course criteria;
4. three-minute field reset;
5. no code edits until the pit period.

During the pit, teams may restore a frozen version or make one documented change. They must state the evidence and risk before editing.

### Session B — Technical defense

Each team presents:

- one route and its phase diagram;
- one feedback controller, including error and gain;
- reliability data and the largest remaining limitation;
- the reason for mission order;
- one code-architecture decision;
- a physical SPIKE Prime transfer plan.

Every student answers two oral-defense questions from the assessment guide.

### Required SPIKE transfer map

| Simulator item | Physical SPIKE decision |
|---|---|
| `EV3Brick` / no hub menu | initialize `PrimeHub`; add hub menu if desired |
| `pybricks.ev3devices` | use `pybricks.pupdevices` |
| ports A/B/C and S1–S4 | map to actual SPIKE A–F wiring and hub IMU |
| 56 mm wheel / 152 mm track | measure, then calibrate actual geometry |
| explicit `GyroSensor` loop | choose hub IMU loop or `DriveBase.use_gyro(True)` |
| synchronous simulator calls | verify current API/firmware call and `await` requirements |
| idealized surface/model | recalibrate light, friction, contact, speed, and attachments |
| constant dispatcher | optionally use SPIYKE-style `hub_menu` |

### Final capstone submission

- frozen multi-module code zip;
- configuration sheet;
- final match plan and scores;
- reliability tables;
- engineering log;
- SPIKE transfer map;
- individual reflection: “one skill I can reproduce without this simulator, one assumption I must re-test on hardware.”

### Final mastery standard

A student has reached course mastery when they can independently modify a mission, predict the effect, run a bounded test, interpret evidence, and explain how to recalibrate the same idea on a physical robot. A high simulator score alone is not mastery.

---

## Appendix A — Pybricks command progression

| Introduced | Command or property | Purpose |
|---:|---|---|
| 1 | `straight(distance)` | encoder-based linear maneuver |
| 1 | `turn(angle)` | encoder-based relative pivot |
| 2 | `settings(speed, accel, rate, turn_accel)` | motion profile |
| 2 | `distance()`, `angle()`, `state()` | observe drive-base estimate |
| 3 | functions and loops | express repeated routes |
| 4 | `drive(speed, turn_rate)`, `stop()` | continuous sensor-driven motion |
| 4 | color/distance/gyro readings | detect field conditions |
| 5 | proportional correction | line control |
| 6 | `reset()` and gyro reference | controlled state origin |
| 7 | `run_angle`, `run_time`, `wait=False` | attachment behavior |
| 8 | modules/imports | competition architecture |
| 12 | physical `arc`, `use_gyro`, stop modes, current async style | post-simulator transfer |

## Appendix B — Instructor-defined capstone scoring

Use this generic scoring when the chosen Gears field does not reproduce official season scoring:

| Objective | Points |
|---|---:|
| Leave home completely | 5 |
| Interact successfully with object A | 20 |
| Interact successfully with object B | 25 |
| Interact successfully with object C | 30 |
| Use a sensor alignment before an objective | 10 |
| Return completely to home | 10 |
| Robot stranded outside home at end | −10 |

Publish the exact observable state for each interaction before Week 9. Do not change scoring after teams begin reliability trials.

## Appendix C — Source links

- [Pybricks Robotics and DriveBase documentation](https://docs.pybricks.com/en/latest/robotics.html)
- [SPIYKE base code](https://github.com/fssfll/spike_basecode)
- [Gears source repository](https://github.com/QuirkyCort/gears)
- [Hosted Gears simulator](https://gears.aposteriori.com.sg/)

The course intentionally teaches the overlap among these sources and labels every known simulator-to-hardware difference.
