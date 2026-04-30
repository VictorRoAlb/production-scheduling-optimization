# Problem Formulation

The public benchmark instance corresponds to a production-planning and scheduling exercise on unrelated parallel machines.

## Core elements

- `N = 50` jobs
- `M = 5` machines
- machine-dependent processing times

## Progressive extensions

The original project reports six extensions:

1. `R || Cmax`
2. `R | rj | Cmax`
3. `R | rj, sijk | Cmax`
4. `R | rj, sijk, prec | Cmax`
5. `R | rj, sijk, prec, res | Cmax`
6. `R | rj, sijk, prec, res | sum(wjTj)`

Where:

- `rj` denotes release dates;
- `sijk` denotes sequence-dependent setup times;
- `prec` denotes precedence constraints;
- `res` denotes shared resource limits;
- `sum(wjTj)` denotes total weighted tardiness.

## Public benchmark assets

The repository includes CSV exports for:

- release dates;
- due dates;
- job weights;
- precedence pairs;
- resource requirements and shared capacity;
- setup matrices for the five machines.

The base Excel workbook is intentionally excluded from the public version.

