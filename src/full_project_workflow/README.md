# Full Project Workflow

This folder contains cleaned public copies of the two main Python scripts from the coursework project.

## Files

- `01_generate_instance_from_workbook.py`
  Expands the base workbook into release dates, setup times, due dates, weights, precedence arcs and resource-capacity data.
- `02_solve_benchmark_extensions.py`
  Solves six benchmark extensions and compares CP-SAT, a genetic algorithm and iterated greedy.

## Important note

The original workbook `R_Cmax.xlsx` is not distributed in this repository.

To run these scripts on your own machine, set:

```powershell
$env:PPP_WORKBOOK_PATH="C:\path\to\R_Cmax.xlsx"
```

The rest of the script paths are derived automatically from that workbook location.
