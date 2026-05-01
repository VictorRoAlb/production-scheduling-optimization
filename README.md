# Production Planning and Parallel Machine Scheduling

Public repository for a production-planning and scheduling coursework project focused on unrelated parallel machines with progressively richer constraint sets.

## Project focus

The original work studies a scheduling benchmark built around:

- unrelated parallel machines;
- release dates;
- sequence-dependent setup times;
- precedence constraints;
- shared resource limits;
- weighted tardiness and makespan objectives;
- comparison between exact and metaheuristic approaches.

## Methods implemented in the coursework

- constructive greedy assignment;
- CP-SAT modelling with OR-Tools;
- genetic algorithm on job permutations;
- iterated greedy with destroy-and-repair logic.

The project is organized as a sequence of six benchmark extensions, moving from the base `R || Cmax` setting to a weighted-tardiness formulation with release dates, setup times, precedence constraints and shared resources.

## Public version

What is intentionally included:

- safe CSV instance files exported from the executed project;
- repository documentation describing the benchmark extensions and modelling choices;
- lightweight public scripts for loading the instance and parsing result summaries;
- cleaned versions of the two main Python scripts used in the academic project;
- a curated summary of computational results.

What is intentionally excluded:

- original Excel workbooks;
- course PDFs and submission documents;
- any local path-bound execution material that is not needed for a public portfolio.

## Repository structure

- `examples/instance_csv/`
  Public-safe CSV instance derived from the original executed project.
- `src/load_public_instance.py`
  Small helper to inspect the exported instance from CSV files.
- `src/parse_resultados_ppp.py`
  Helper to parse the computational-results text file format used in the original project.
- `src/full_project_workflow/`
  Cleaned versions of the original project scripts:
  - `01_generate_instance_from_workbook.py`
  - `02_solve_benchmark_extensions.py`
- `results/computational_results_summary.md`
  Curated summary of the six benchmark extensions.
- `docs/`
  Notes on the problem formulation, algorithmic workflow and publication decisions.

## Computational setting captured in the original project

- `CP-SAT`
- `Genetic algorithm`
- `Iterated greedy`

Across the stored benchmark summary, the iterated-greedy implementation was the best-performing method on all six reported extensions of the public result set.

## What the public code now shows

The public repository exposes the actual implementation logic used in the coursework:

- how the Excel-based benchmark was expanded into release dates, setups, due dates, precedence arcs and resource capacities;
- how the same benchmark was solved under six increasingly constrained scenarios;
- how CP-SAT, a genetic algorithm and iterated greedy were compared on the same instance;
- how result summaries, RPD calculations and machine-wise sequences were reported.

## Data availability

The original Excel workbook used to define and execute the full coursework instance is not published here. The public repository ships only CSV exports that are sufficient to document the benchmark structure safely.

If you want to execute the full workflow exactly as staged in the coursework, you must provide your own compatible workbook locally and point the environment variable `PPP_WORKBOOK_PATH` to it.

## Recommended reading order

1. `docs/problem_formulation.md`
2. `docs/algorithmic_workflow.md`
3. `results/computational_results_summary.md`
4. `src/full_project_workflow/`

## Publication notes

This repository was rebuilt from the stronger source folder after review. The public version avoids uploading spreadsheets and focuses on the technical problem structure, solver framing, algorithmic implementation and results narrative.
