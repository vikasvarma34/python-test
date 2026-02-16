PYTHON + NUMPY + PANDAS (14-DAY JOB-READY PLAN) — UNIFORM WORKLOAD EDITION
Date: 2026-02-16
Purpose: Build the exact Python + NumPy + pandas foundation expected before starting Google’s Machine Learning Crash Course, with job-real implementation focus.
Primary prerequisite reference: Google ML Crash Course “Prereqs and prework”. (Link in SOURCES)

============================================================
MANDATORY TEACHING / EXPLANATION STYLE (READ THIS FIRST)
Whenever you explain anything from this plan (concepts, APIs, best practices, examples, errors, tradeoffs), follow these rules:

1) Use the internet every time (plus your own knowledge)
- Always look up the topic online before explaining it.
- Use your own understanding to connect the dots, but do not “guess” APIs/behavior from memory.
- If something changed recently (library versions, defaults, edge cases), treat the internet as the source of truth.

2) Only use reliable sources (no random blogs)
Prioritize sources in this order:
- Official documentation (Python docs, NumPy docs, pandas docs)
- Google official docs + Google Python Style Guide
- PEPs for Python conventions (especially PEP 8 for style)
- Widely trusted engineering references (only when official docs are missing something)
Avoid:
- Medium-style personal blogs, SEO spam, “top 10 tips” posts with no authority
- Anything that looks outdated, copy-pasted, or not maintained

3) Explain in “job-real” detail (not shortcuts, not toy examples)
When you teach a topic, include:
- What it is (definition in plain language)
- Where it shows up in real work (pipelines, APIs, ETL, data cleaning, production scripts)
- The common mistakes and failure modes
- The correct patterns (what professionals typically do)
- When NOT to use it (tradeoffs)

4) Give multiple examples and compare to Java/JavaScript
For every major concept, provide:
- At least 2–3 examples:
  - one “simple to understand”
  - one “realistic work scenario”
  - one “edge case / failure case”
- A quick comparison to how you’d do it in Java/JS when that helps (so differences are obvious).

5) Be systematic: from basics → patterns → pitfalls → practice
Use this structure when explaining:
- Core idea
- Typical usage
- Pitfalls (and how to avoid)
- Debug tips (how to read the error / what to print/log)
- A short practice checklist (“If you can do these, you understood it”)

6) Prefer reusable, clean code patterns
- Encourage small functions, clear names, typing where it helps, and predictable behavior.
- Keep “pure logic” separate from “side effects” (file/network/time).
- Show how to structure code in modules (src/app/...) instead of writing everything in one file.

7) No unnecessary file creation — keep outputs inside the existing project
- Do NOT create extra files unless the plan explicitly asks for them.
- Do NOT create random .md/.txt/.exe “notes” files.
- If you need to provide notes, put them directly in the explanation output or in THIS SAME plan file under the “Notes / Problems” section for that day.
- If you need sample data, prefer inline examples first. Only create sample files if the day’s deliverables explicitly require using /data.

8) Be strict about correctness and clarity
- If there are multiple valid ways (e.g., requests vs httpx, dataclasses vs pydantic), explain the decision criteria.
- If sources disagree, pick the most authoritative/current option and say why (without turning it into a long debate).
- Never hide uncertainty: if something depends on version or context, say what it depends on and how to verify.

9) Keep it focused on this 14-day plan
- Tie explanations back to what the user is building TODAY (module + script + tests).
- Do not wander into unrelated topics unless the user asks.
- End every explanation with “Next actions” that map to today’s checklist items.
============================================================

HOW THIS PLAN STAYS “UNIFORM” (IMPORTANT)
Each day is designed to be comparable in effort. Every day includes:
A) Language/library topics (roughly the same number of topic blocks)
B) A concrete build artifact set:
   - 1 module (reusable code under /src/app/...)
   - 1 script (under /scripts/...)
   - 1 test file (under /tests/...)
C) A small “notes + checklist” update inside this file
No day is meant to be “too light” or “too heavy.” If any day feels too small, expand the deliverables by adding extra edge cases + tests (NOT random extra topics).

PROJECT FOLDER SHAPE (KEEP STABLE FOR 14 DAYS)
- /src/app
  - /core        (config, logging, utilities)
  - /models      (dataclasses/pydantic models)
  - /services    (IO, APIs, pipelines)
- /scripts       (CLI entry points)
- /tests         (pytest)
- /data          (small sample inputs/outputs)
- README.md      (how to run + how to test)

PROGRESS TRACKING (EDIT DAILY)
TODAY: Day __ / 14
DATE:
STATUS: Started / In Progress / Done
What I built:
What confused me:
What to revisit:
Next steps:

============================================================
RELIABLE SOURCES WHITELIST (USE THESE FIRST)
1) Google ML Crash Course — Prereqs & prework:
   https://developers.google.com/machine-learning/crash-course/prereqs-and-prework

2) Python official docs — The Python Tutorial:
   https://docs.python.org/3/tutorial/index.html
   (Key chapters you will frequently reference: Data Structures, Modules, Errors/Exceptions, Classes)

3) NumPy official docs — Quickstart + Indexing + Ufuncs:
   https://numpy.org/doc/stable/user/quickstart.html
   https://numpy.org/devdocs/user/basics.indexing.html
   https://numpy.org/doc/2.1/user/basics.ufuncs.html

4) pandas official docs — User Guide + Indexing + Missing Data:
   https://pandas.pydata.org/docs/user_guide/index.html
   https://pandas.pydata.org/docs/user_guide/indexing.html
   https://pandas.pydata.org/docs/user_guide/missing_data.html
============================================================

========================
DAY 1 — PROJECT + ENV + “RUNNABLE” PYTHON (NOT BASIC)
Syllabus topics (cover all):
- Environment + dependency management workflow (venv/pip OR poetry/uv) and pinning
- Running code properly: scripts vs modules (python -m), import paths, packaging layout
- Coding standards baseline: formatting + linting + type hints strategy
- Minimal logging strategy (so your scripts are debug-friendly from day 1)
- Basic repo hygiene: README, .gitignore, folder structure conventions

Build artifacts (must exist):
- /src/app/core/runtime.py
  - responsibilities: basic “runtime utilities” (paths, environment detection, safe exits)
- /scripts/healthcheck.py
  - prints a structured “project OK” output and confirms imports work
- /tests/test_healthcheck.py
  - tests core utilities used by the healthcheck

Checklist:
- [ ] Environment created and reproducible
- [ ] Imports work without sys.path hacks
- [ ] README has setup + run + test commands

========================
DAY 2 — PYTHON DATA TYPES + CONTROL FLOW (ML PREWORK CORE)
Syllabus topics (cover all):
- Built-in types you must be fluent in: int/float/bool/str
- Strings: slicing, f-strings, formatting, common gotchas
- Collections: list/tuple/set/dict (when to use which)
- Comprehensions (list/dict/set) and readable iteration patterns
- Truthiness, equality vs identity, common runtime mistakes

Build artifacts:
- /src/app/core/primitives.py
  - responsibilities: helpers for parsing/normalizing common primitives (strings, numbers)
- /scripts/normalize_records.py
  - reads a small JSON list of records -> normalizes fields -> outputs cleaned JSON
- /tests/test_primitives.py

Checklist:
- [ ] Confident with dict/list transforms without over-looping
- [ ] Clean normalization output + predictable errors on bad input

========================
DAY 3 — FUNCTIONS + MODULES + ERROR STYLE (BACKEND-QUALITY PYTHON)
Syllabus topics:
- Functions: signatures, defaults (mutable default pitfall), *args/**kwargs usage patterns
- Designing functions for testability (pure core vs I/O wrappers)
- Modules/packages: organizing code, avoiding circular imports
- Exceptions: standard exception types + when to raise vs return
- Writing error messages with context (so debugging is fast)

Build artifacts:
- /src/app/core/errors.py
  - responsibilities: custom exceptions + error helpers
- /scripts/validate_input.py
  - validates a sample file, raises friendly errors
- /tests/test_errors_and_validation.py

Checklist:
- [ ] Consistent error style across scripts
- [ ] Tests cover at least 6 failure modes

========================
DAY 4 — DATA MODELS + TYPING (STRUCTURE YOUR DATA LIKE A PRO)
Syllabus topics:
- dataclasses (or pydantic if you choose it) for models
- Type hints used in real code: Optional/Union/Literal, generics, TypedDict (where useful)
- Validation boundaries: validate at the edge, keep core logic clean
- Serialization: model <-> dict/JSON
- Modeling ML/analytics-friendly data: numeric fields, categories, timestamps

Build artifacts:
- /src/app/models/schemas.py
  - responsibilities: 4–8 models (raw input, cleaned row, report row, etc.)
- /scripts/model_roundtrip.py
  - loads raw -> model -> dict -> model again, proves round-trip safety
- /tests/test_models_roundtrip_and_validation.py

Checklist:
- [ ] Models reject invalid inputs clearly
- [ ] Round-trip works for clean data

========================
DAY 5 — FILE I/O + FORMATS (CSV/JSON/NDJSON) + STREAMING THINKING
Syllabus topics:
- pathlib best practices for file paths
- Reading/writing JSON and CSV reliably (encoding, newline, types)
- NDJSON pattern (line-delimited JSON)
- Streaming vs loading whole file (generator mindset)
- Data “contracts”: required columns/keys and schema checks

Build artifacts:
- /src/app/services/io.py
  - responsibilities: read_csv/read_json/read_ndjson + write equivalents + schema checks
- /scripts/ingest.py
  - ingest -> validate -> write normalized output
- /tests/test_io_ingest.py

Checklist:
- [ ] Supports at least CSV + JSON (NDJSON optional but preferred)
- [ ] Handles missing required fields with good errors

========================
DAY 6 — HTTP / API CLIENT BASICS (JOB INTEGRATIONS)
Syllabus topics:
- HTTP client patterns (requests/httpx conceptually) + timeouts
- Retries/backoff basics + when NOT to retry
- Auth patterns: API key / bearer token
- Pagination patterns and error mapping
- Parsing API responses into your models

Build artifacts:
- /src/app/services/api_client.py
  - responsibilities: one clean client with timeouts + error mapping
- /scripts/fetch_and_store.py
  - fetches sample data (real or mocked) -> stores JSON -> validates into models
- /tests/test_api_client_mocked.py (no real network in tests)

Checklist:
- [ ] Clear exception types: auth failure vs retryable vs bad payload
- [ ] Models validate API payloads

========================
DAY 7 — NUMPY CORE: NDARRAY MENTAL MODEL + SHAPE/AXIS
Syllabus topics:
- ndarray fundamentals: dtype, shape, ndim, axis
- Creating arrays: zeros/ones/arange/linspace/random basics
- Indexing/slicing for 1D/2D
- reshape/transpose/stack/concat
- view vs copy (mutation surprises)
- Vectorization mindset (avoid Python loops for numeric ops)

Build artifacts:
- /src/app/services/numpy_core.py
  - responsibilities: reusable numeric transforms + shape-safe helpers
- /scripts/numpy_workbook.py
  - demonstrates creation, slicing, reshape, join, and a small numeric transform pipeline
- /tests/test_numpy_core.py

Checklist:
- [ ] You can explain axis=0 vs axis=1 and prove it with code
- [ ] You can reshape safely without guessing

========================
DAY 8 — NUMPY POWER: BROADCASTING + UFUNCS + MASKING + AGGS
Syllabus topics:
- Broadcasting rules (practical usage)
- ufuncs (element-wise ops) + where/clip
- Boolean masks and filtering
- Aggregations over axes (sum/mean/std/min/max)
- Numeric stability basics (dtype issues, overflow awareness)
- Performance basics (why vectorization matters)

Build artifacts:
- /src/app/services/numpy_ops.py
  - responsibilities: masked transforms + aggregations
- /scripts/numpy_features.py
  - builds a small “feature table” from numeric arrays (ready to become DataFrame later)
- /tests/test_numpy_ops.py

Checklist:
- [ ] You can build features without loops for core computations
- [ ] Tests cover edge cases (empty mask, all missing, weird shapes)

========================
DAY 9 — PANDAS FUNDAMENTALS: SERIES/DATAFRAME + LOADING + INSPECTION
Syllabus topics:
- Series vs DataFrame
- Index basics (what it is, why it matters)
- Reading data: read_csv/read_json + dtype considerations
- Inspecting data: head/info/describe/value_counts
- Column operations: rename, astype, vectorized string ops
- Selection basics: loc/iloc/boolean indexing (conceptual + practical)

Build artifacts:
- /src/app/services/pandas_load.py
  - responsibilities: load + standardize columns + basic profiling summary
- /scripts/profile_dataset.py
  - loads dataset -> prints consistent profile report -> exports cleaned copy
- /tests/test_pandas_load_profile.py

Checklist:
- [ ] You can select/filter correctly without “mystery behavior”
- [ ] You can standardize schema across two inputs

========================
DAY 10 — PANDAS REAL WORK: GROUPBY + JOINS + RESHAPE
Syllabus topics:
- groupby aggregations + multi-agg
- merge/join strategies: keys, duplicates, left vs inner logic
- pivot/melt for wide/long reshaping
- sorting and ranking basics
- building “report tables” reliably

Build artifacts:
- /src/app/services/pandas_transform.py
  - responsibilities: join + aggregate + reshape pipeline
- /scripts/build_report.py
  - reads two inputs -> merges -> aggregates -> outputs a report CSV/JSON
- /tests/test_pandas_transform_report.py

Checklist:
- [ ] You can explain your join keys and prove correctness with tests
- [ ] Report output is deterministic

========================
DAY 11 — PANDAS DATA QUALITY: MISSING DATA + DUPLICATES + RULES
Syllabus topics:
- Missing representations: NaN/NA/None/NaT (awareness)
- Detecting missing: isna/notna
- Handling: dropna/fillna, forward/back fill (when appropriate)
- Duplicates: detection and handling
- Data quality rules: ranges, required fields, schema enforcement
- “Fail vs fix” strategy (when to stop the pipeline)

Build artifacts:
- /src/app/services/data_quality.py
  - responsibilities: enforce rules + produce quality summary (counts of issues)
- /scripts/quality_check.py
  - runs checks and outputs a quality report
- /tests/test_data_quality_rules.py

Checklist:
- [ ] Rules are explicit and test-covered
- [ ] Quality report is clear and actionable

========================
DAY 12 — TIME + TEXT IN DATA (ALWAYS SHOWS UP IN ML/DATA JOBS)
Syllabus topics:
- Datetime parsing in pandas (including messy inputs)
- Timezone awareness concept + standardization approach
- DatetimeIndex usage + time filtering
- resampling basics (daily/weekly/monthly)
- rolling windows basics
- text cleaning basics (vectorized string ops, normalization)

Build artifacts:
- /src/app/services/time_text.py
  - responsibilities: parse dates + standardize + time-based aggregations + text normalization helpers
- /scripts/time_series_report.py
  - reads time-based dataset -> standardizes -> outputs resampled/rolling metrics
- /tests/test_time_text.py

Checklist:
- [ ] You can standardize timestamps and prove correctness with tests
- [ ] You can produce time-bucketed metrics reliably

========================
DAY 13 — PRODUCTION PRACTICES: TESTING + LOGGING + CONFIG + CLI
Syllabus topics:
- pytest: fixtures, parametrization, mocking I/O and API calls
- logging module: consistent format + module loggers
- config loading from env + validation
- CLI design (argparse/typer/click conceptually) + subcommands
- packaging awareness: python -m, entry points concept

Build artifacts:
- /src/app/core/config.py + /src/app/core/logging.py
  - responsibilities: validated config + reusable logger setup
- /scripts/tool.py
  - real CLI: subcommands for ingest/profile/report/quality (as many as you already built)
- /tests/test_cli_and_config.py

Checklist:
- [ ] Scripts run with config + logging consistently
- [ ] CLI errors are user-friendly (exit codes + messages)

========================
DAY 14 — CAPSTONE: ML-PREWORK PIPELINE (PYTHON + NUMPY + PANDAS TOGETHER)
Pick ONE capstone (choose the most job-relevant):
A) Ingest -> Clean -> Feature Table (NumPy features + pandas output)
B) API -> Normalize -> Join -> Report (models + pandas groupby/merge)
C) NDJSON Logs -> Parse -> Time buckets -> Quality report

Syllabus topics (must show up in the capstone):
- Clean architecture boundaries (core/models/services/scripts/tests)
- Strong validation at boundaries (input + API payload)
- NumPy features or numeric transforms (vectorized)
- pandas pipeline (load/select/groupby/merge/missing handling)
- Tests for critical transformations
- README polish: how to run + how to test + common failures

Build artifacts:
- /src/app/services/capstone_pipeline.py
- /scripts/capstone.py (CLI)
- /tests/test_capstone_end_to_end.py

Checklist:
- [ ] One command runs the full pipeline and produces outputs
- [ ] Test suite protects the most important logic
- [ ] README is clear enough for someone else to use it

============================================================
SELF-CHECK: READY FOR ML CRASH COURSE PREWORK WHEN YOU CAN DO:
- Python basics listed by Google MLCC (functions, dict/list/set, loops, string formatting, list comprehensions)
- NumPy array fundamentals (shape/axis, indexing, vectorized ops, broadcasting/ufuncs)
- pandas essentials (indexing/selecting, groupby, merges, missing-data handling)
(Use the official sources above whenever you need a refresher.)
============================================================
END
