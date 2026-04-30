# Computational Results Summary

The original executed project reported six extensions. The summary below is based on the stored text output exported from the full local project.

## Extension overview

| Extension | Formulation | Best method | Best objective | Best time (s) |
| --- | --- | --- | ---: | ---: |
| 0 | `R || Cmax` | Iterated Greedy | 168.00 | 78.86 |
| 1 | `R | rj | Cmax` | Iterated Greedy | 169.00 | 83.45 |
| 2 | `R | rj, sijk | Cmax` | Iterated Greedy | 195.00 | 94.65 |
| 3 | `R | rj, sijk, prec | Cmax` | Iterated Greedy | 197.00 | 214.80 |
| 4 | `R | rj, sijk, prec, res | Cmax` | Iterated Greedy | 199.00 | 2191.15 |
| 5 | `R | rj, sijk, prec, res | sum(wjTj)` | Iterated Greedy | 3060.00 | 5640.78 |

## Method comparison snapshot

### Extension 0 — `R || Cmax`

- Iterated Greedy: `168.00`
- Genetic algorithm: `170.00`
- CP-SAT: `200.00`

### Extension 1 — `R | rj | Cmax`

- Iterated Greedy: `169.00`
- Genetic algorithm: `171.00`
- CP-SAT: `194.00`

### Extension 2 — `R | rj, sijk | Cmax`

- Iterated Greedy: `195.00`
- Genetic algorithm: `209.00`
- CP-SAT: `670.00`

### Extension 3 — `R | rj, sijk, prec | Cmax`

- Iterated Greedy: `197.00`
- Genetic algorithm: `219.00`
- CP-SAT: `230.00`

### Extension 4 — `R | rj, sijk, prec, res | Cmax`

- Iterated Greedy: `199.00`
- Genetic algorithm: `228.00`
- CP-SAT: `263.00`

### Extension 5 — `R | rj, sijk, prec, res | sum(wjTj)`

- Iterated Greedy: `3060.00`
- Genetic algorithm: `4426.00`
- CP-SAT: `7361.00`

## Public note

The full local result file also stores machine-by-machine sequences and relative-gap values. In this public export, the emphasis is placed on the benchmark extensions and method-level performance summary.

