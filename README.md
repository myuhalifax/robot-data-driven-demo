# Robot Framework — Data-Driven System Testing Demo

A small, runnable model of **system-level** (non-web) test automation:
a program is driven with data files, and its outputs + logs are verified.
This mirrors defence/industrial Linux testing: feed the system simulated
data, check the results and the evidence (logs), repeat across data sets.

## Layers (who writes code, who doesn't)
- `tests/` — test cases: **keywords + data only, no code.** Data-driven
  rows: one line per data set (the layer Derek worked in).
- `resources/common.robot` — reusable high-level keywords.
- `libraries/ProcessorLibrary.py` — the framework layer: **Python code**
  that drives the system under test (written/maintained by whoever owns
  the framework; extended when interfaces change).
- `app/processor.py` — a stand-in "system under test" (a sonar-like
  contact classifier): data in -> summary.txt + app.log out.
- `data/` — input data sets (CSV). New scenario = new file + one row.

## Run it
    python3 -m venv .venv && .venv/bin/pip install robotframework
    .venv/bin/robot -d results/report tests/

HTML report lands in `results/report/report.html`.

## Talking point
"I worked on an existing keyword-driven Robot Framework, writing
data-driven test cases. The framework layer was Python — I can read and
extend Python keywords when I need to."
