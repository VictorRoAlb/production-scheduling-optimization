# Algorithmic Workflow

This public repository keeps the original structure of the coursework project while removing the private workbook.

## 1. Instance generation

`src/full_project_workflow/01_generate_instance_from_workbook.py` starts from the base processing-time table and expands the instance with:

- release dates;
- sequence-dependent setup times;
- due dates;
- job weights;
- precedence pairs;
- resource requirements and total staff capacity.

The generation stage uses fixed random seeds so that the academic benchmark remains reproducible.

## 2. Progressive benchmark extensions

`src/full_project_workflow/02_solve_benchmark_extensions.py` solves the same instance under six scenarios:

1. `R || Cmax`
2. `R | rj | Cmax`
3. `R | rj, sijk | Cmax`
4. `R | rj, sijk, prec | Cmax`
5. `R | rj, sijk, prec, res | Cmax`
6. `R | rj, sijk, prec, res, dj | sum(wjTj)`

This structure makes the project easy to read from an academic perspective because each extension activates one more layer of realism.

## 3. Constructive evaluation

The solver script relies on a constructive evaluator that:

- starts from a job permutation;
- checks release dates and precedence relations;
- assigns each job to the machine with the best greedy completion time;
- accounts for setup times when active;
- waits for staff capacity when the resource extension is enabled;
- computes either makespan or weighted tardiness depending on the active objective.

This same constructive block is reused by the metaheuristics.

## 4. CP-SAT model

The exact approach uses OR-Tools CP-SAT with:

- binary assignment variables;
- job start and completion variables;
- disjunctive sequencing logic on each machine;
- optional cumulative-resource constraints;
- precedence constraints;
- either `Cmax` or weighted tardiness as the objective.

## 5. Genetic algorithm

The genetic algorithm is permutation-based and includes:

- mixed initialization around a release-aware base permutation;
- tournament selection;
- order crossover;
- swap and inversion mutation;
- elitism;
- repair of precedence violations when needed.

## 6. Iterated greedy

The iterated-greedy stage uses a classical destroy-and-repair scheme:

- start from a good incumbent permutation;
- remove a subset of jobs;
- reinsert them greedily;
- keep improvements and stop after a patience limit.

According to the stored result file, this method was the strongest performer across all six reported extensions.

## 7. Public vs original material

Published:

- safe CSV exports of the executed instance;
- the cleaned Python scripts;
- parsed result summaries;
- public documentation.

Not published:

- the original workbook;
- classroom PDFs;
- submission files;
- local execution artifacts not needed to understand the project.
