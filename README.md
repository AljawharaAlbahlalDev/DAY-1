# SDA-AIE-211 — Bayan Starter

Bayan is the evolving Arabic/English citizen-feedback NLP application used across the course.
This repository is intentionally incomplete: each lab adds a production component and evidence.

## Golden thread

- Lab 1 → versioned preprocessing + tokenizer decision
- Lab 2 → attention/transformer reasoning + architecture decisions
- Lab 3 → topic/sentiment classifier + NER + QA
- Lab 4 → Arabic profiles + dialect-aware model
- Lab 5 → bilingual semantic search + FAISS + re-ranking
- Lab 6 → sliced evaluation + behavioural tests + error report
- Lab 7 → ONNX/INT8 optimisation + FastAPI serving
- Capstone → integrate the components + one extension

---

# Day 1 — Before the Lab

Each participant must work from **their own GitHub repository** created from the course template.
Do not work directly in the instructor/course repository.

## 1. Create your own repository

1. Open the course GitHub repository shared by the instructor.
2. Click **Use this template** → **Create a new repository**.
3. Create the repository under your own GitHub account.
4. Copy the HTTPS URL of your new repository.

Example:

```text
https://github.com/<YOUR_USERNAME>/SDA-AIE-211-Bayan.git
```

## 2. Clone your repository

```bash
git clone https://github.com/<YOUR_USERNAME>/SDA-AIE-211-Bayan.git
cd SDA-AIE-211-Bayan
```

---

# macOS Setup

## Prerequisites

Confirm Git and Python 3.12 are available:

```bash
git --version
python3.12 --version
```

Expected Python version:

```text
Python 3.12.x
```

If `python3.12` is not found, install Python 3.12 before continuing.

## Create and activate the virtual environment

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

After activation, your terminal should show `(.venv)`.

Upgrade pip and install the course dependencies:
- transformers
- datasets
- sentence-transformers
- spacy
- camel-tools
- scikit-learn
- seqeval
- faiss-cpu
- optimum[onnxruntime]
- fastapi
- uvicorn
- pytest
- pandas
- matplotlib

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run the environment check:

```bash
python scripts/doctor.py
```

Then run the Lab 1 tests:

```bash
pytest -q
```

The Lab 1 preprocessing tests are **expected to fail at the beginning** because the starter implementation contains TODOs. Your goal during Lab 1 is to make them pass.

---

# Windows Setup — PowerShell

## Prerequisites

Confirm Git and Python 3.12 are available:

```powershell
git --version
py -3.12 --version
```

Expected Python version:

```text
Python 3.12.x
```

If `py -3.12` is not found, install Python 3.12 before continuing and make sure the Python Launcher is enabled during installation.

## Create and activate the virtual environment

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation with an execution-policy message, run this once in the current terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

After activation, your terminal should show `(.venv)`.

Upgrade pip and install the course dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run the environment check:

```powershell
python scripts/doctor.py
```

Then run the Lab 1 tests:

```powershell
pytest -q
```

The Lab 1 preprocessing tests are **expected to fail at the beginning** because the starter implementation contains TODOs. Your goal during Lab 1 is to make them pass.

> Windows note: `make` is not required on Day 1. Use `python scripts/doctor.py` and `pytest -q`. The course may use `make` later when available in the classroom environment.

---

# Day 1 Checklist

Before Lab 1 starts, make sure all of the following are true:

- [ ] GitHub account is active.
- [ ] Your own Bayan repository has been created from the template.
- [ ] The repository has been cloned to your computer.
- [ ] Python 3.12 is installed.
- [ ] `.venv` is created and activated.
- [ ] `pip install -r requirements.txt` completed successfully.
- [ ] `python scripts/doctor.py` prints `ALL GOOD`.
- [ ] `pytest -q` starts successfully (failing Lab 1 TODO tests are expected initially).

If `doctor.py` reports a failed check, fix it before starting the lab or ask the instructor for the fallback route.

---

# Lab 1 — What you will complete

During Lab 1 you will:

1. Inspect `data/raw/bayan_raw_sample.csv` and document at least six text-defect classes in `NOTES.md`.
2. Implement `normalize()` and `mask_pii()` in the versioned preprocessing module under `src/bayan/preprocessing/`.
3. Pass the golden preprocessing tests and verify 100% PII recall on the provided fixture.
4. Build and validate the spaCy sentence-segmentation pipeline.
5. Audit four candidate tokenizers and record fertility and p95 sequence-length results by language.
6. Document the tokenizer/model decision with evidence in `DECISIONS.md#tokenizer`.
7. Commit and push your Lab 1 work to your own GitHub repository.

At the end of the lab:

```bash
git status
git add .
git commit -m "feat: complete Lab 1 preprocessing and tokenizer audit"
git push
```

---

# Git discipline

Work in your own GitHub repository created from the course starter/template. Commit after every lab.
Do not copy reference benchmark numbers into `BENCHMARKS.md`; record results from your own runs.

Recommended pattern:

```text
Day 1 → complete lab → test → commit → push
Day 2 → complete lab → test → commit → push
Day 3 → complete lab → test → commit → push
Day 4 → integrate Capstone → test → commit → push
```

# Final service target

By Day 4, the same repository will contain the components built across Labs 1–7.
The final target is an integrated Bayan service that can be started after the required artifacts have been built.
