# Production Planning and Parallel Machine Scheduling

Curated public repository for a production-planning and scheduling coursework project focused on a parallel-machine environment with progressive constraint extensions.

## Project focus

The original work studies a scheduling benchmark built around:

- unrelated parallel machines;
- release dates;
- sequence-dependent setup times;
- precedence constraints;
- shared resource limits;
- weighted tardiness and makespan objectives;
- comparison between exact and metaheuristic approaches.

## Public version

This repository is a cleaned public export prepared from the full project folder `Trabajo Completo PPP`.

What is intentionally included:

- safe CSV instance files exported from the executed project;
- repository documentation describing the benchmark extensions;
- lightweight public scripts for loading the instance and parsing result summaries;
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
- `results/computational_results_summary.md`
  Curated summary of the six benchmark extensions.
- `docs/`
  Notes on the problem formulation and publication decisions.

## Computational setting captured in the original project

- `CP-SAT`
- `Genetic algorithm`
- `Iterated greedy`

Across the stored benchmark summary, the iterated-greedy implementation was the best-performing method on all six reported extensions of the public result set.

## Data availability

The original Excel workbook used to define and execute the full coursework instance is not published here. The public repository ships only CSV exports that are sufficient to document the benchmark structure safely.

## Publication notes

This repository was intentionally rebuilt from the better source folder after review. The public version avoids uploading spreadsheets and focuses on the technical problem structure, solver framing and results narrative.

