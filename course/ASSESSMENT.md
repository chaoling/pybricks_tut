# Assessment and Rubrics

## Weighting

| Category | Weight |
|---|---:|
| Weekly skill checks (Weeks 1–8) | 25% |
| Engineering log and test evidence | 20% |
| Week 6 controller checkpoint | 15% |
| Week 11 reliability review | 15% |
| Week 12 capstone | 25% |

## Weekly skill-check scale

- **4 — Mastery:** works across five trials, code is readable/reusable, and the student explains why it works.
- **3 — Proficient:** works across four of five trials and the student can trace the code.
- **2 — Developing:** works inconsistently or only with coaching; explanation is partial.
- **1 — Beginning:** a runnable attempt exists but does not yet meet the target.
- **0 — No evidence:** no runnable attempt or explanation.

## Controller checkpoint — 60 points

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Sensor calibration | 10 | measured light/dark or heading baseline; threshold/setpoint justified |
| Control math | 15 | error, gain, correction, and steering signs are correct |
| Loop safety | 10 | short wait, clear exit condition, and timeout/distance limit |
| Tuning process | 10 | one-variable trials with evidence, not guess-and-replace |
| Performance | 10 | meets the stated course tolerance in 4/5 trials |
| Explanation | 5 | student can predict behavior when gain or speed changes |

## Reliability review — 60 points

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Acceptance criteria | 5 | observable success and tolerance defined before testing |
| Repeated trials | 15 | ten trials recorded with unchanged code |
| Perturbation tests | 10 | at least two controlled start/physics variations |
| Failure classification | 10 | failures tagged (launch, navigation, contact, attachment, timing, code) |
| Improvement decision | 10 | highest-impact failure addressed with evidence |
| Honest conclusion | 10 | claim matches data; limitations are stated |

## Final capstone — 100 points

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Mission performance | 25 | at least three FLL-style objectives completed in a timed run |
| Reliability | 20 | at least 8/10 successful pre-match runs on each scored route |
| Navigation and sensor use | 15 | appropriate distance, turn, line, gyro, or distance feedback choices |
| Architecture | 15 | configuration separated from mission files; meaningful functions/constants; clean entry point |
| Testing evidence | 10 | versioned log with hypotheses, results, and one-variable changes |
| Readability | 5 | names, comments, units, and formatting allow another team to maintain it |
| Oral defense | 5 | each student explains one algorithm and one tradeoff |
| SPIKE transfer plan | 5 | identifies imports, ports, dimensions, gyro, call-style, and recalibration changes |

## Capstone minimum requirements

- `main.py`, `robot.py`, and at least three mission modules;
- no unbounded sensor loop;
- no unexplained “magic number” in mission logic;
- at least one sensor-controlled behavior;
- at least one attachment action overlapped with or coordinated with driving;
- a timed 150-second match plan with a recovery choice;
- a ten-trial reliability table for every route used in the final match.

## Individual oral-defense prompts

Ask each student two at random:

1. Why does wheel diameter change reported distance?
2. What does axle track change during a turn?
3. Predict what happens if `KP` doubles.
4. Why should a sensor loop contain both a delay and an exit limit?
5. When is a line alignment better than an encoder-only approach?
6. Why split missions into separate files?
7. Which simulator assumption is most likely to fail on hardware?
8. Show where you would change ports and physical dimensions.
9. Explain one failed trial and the evidence behind your fix.
10. Which route would you abandon during a match, and why?
