from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_01 = ROOT / "src" / "full_project_workflow" / "01_generate_instance_from_workbook.py"
SCRIPT_02 = ROOT / "src" / "full_project_workflow" / "02_solve_benchmark_extensions.py"
NOTEBOOKS_DIR = ROOT / "notebooks"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def slice_text(text: str, start: str, end: str | None = None) -> str:
    start_idx = text.index(start)
    end_idx = text.index(end, start_idx) if end else len(text)
    chunk = text[start_idx:end_idx].strip("\n")
    return chunk + "\n"


def to_source_lines(text: str) -> list[str]:
    return [line + "\n" for line in text.rstrip("\n").splitlines()]


def md_cell(text: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": to_source_lines(text),
    }


def code_cell(text: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": to_source_lines(text),
    }


def notebook(cells: list[dict]) -> dict:
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "version": "3.x",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def build_instance_generation_notebook(script_text: str) -> dict:
    imports_cfg = slice_text(
        script_text,
        "import os, csv, random",
        "# ══════════════════════════════════════════════════════════════════════════════\n# 1. LEER TIEMPOS DE PROCESO DESDE EL EXCEL",
    )
    read_processing = slice_text(
        script_text,
        "def leer_tiempos_proceso():",
        "# ══════════════════════════════════════════════════════════════════════════════\n# 2. GENERADORES DE PARÁMETROS",
    )
    generators = slice_text(
        script_text,
        "def generar_releases():",
        "# ══════════════════════════════════════════════════════════════════════════════\n# 3. ESCRIBIR EN EXCEL Y GUARDAR CSVs",
    )
    write_outputs = slice_text(
        script_text,
        "def _hoja_nueva(wb, nombre):",
        "# ══════════════════════════════════════════════════════════════════════════════\n# 4. MAIN",
    )
    main_block = slice_text(script_text, 'if __name__ == "__main__":')

    cells = [
        md_cell(
            "# PPP notebook 01 — Instance generation\n\n"
            "This notebook mirrors the data-generation stage used in the project.\n\n"
            "It starts from the base processing-time workbook and expands the benchmark with:\n"
            "- release dates;\n"
            "- setup times;\n"
            "- due dates and weights;\n"
            "- precedence arcs;\n"
            "- resource-capacity parameters.\n\n"
            "The original workbook is not distributed in the public repository, but the code below is the cleaned execution version used to build the instance."
        ),
        md_cell(
            "## Imports and configuration\n\n"
            "The execution path is controlled through `PPP_WORKBOOK_PATH`. "
            "All CSV outputs are written next to the workbook so the generated instance can later be solved under the six benchmark extensions."
        ),
        code_cell(imports_cfg),
        md_cell(
            "## Reading the processing-time table\n\n"
            "The project starts from the base unrelated-parallel-machine table stored in the workbook."
        ),
        code_cell(read_processing),
        md_cell(
            "## Generating additional benchmark parameters\n\n"
            "This block adds all the realism layers used later in the scheduling benchmark: releases, setups, due dates, priorities, precedences and shared-resource requirements."
        ),
        code_cell(generators),
        md_cell(
            "## Writing the generated instance\n\n"
            "The generated data are written back to workbook sheets and also exported as CSV files."
        ),
        code_cell(write_outputs),
        md_cell(
            "## Execution entry point\n\n"
            "This is the one-shot generation stage that must be run before solving the extensions."
        ),
        code_cell(main_block),
    ]
    return notebook(cells)


def build_benchmark_execution_notebook(script_text: str) -> dict:
    imports_cfg = slice_text(
        script_text,
        "import time, random, json, os",
        "# ══════════════════════════════════════════════════════════════════════════════\n# BLOQUE 1 — LECTURA DE DATOS",
    )
    load_data = slice_text(
        script_text,
        "def cargar_datos():",
        "# ══════════════════════════════════════════════════════════════════════════════\n# BLOQUE 2 — FUNCIÓN CONSTRUCTIVA GREEDY",
    )
    constructive = slice_text(
        script_text,
        "def _esperar_recursos(t_prop, h_j, H, activos, duracion):",
        "# ══════════════════════════════════════════════════════════════════════════════\n# BLOQUE 3 — CP-SAT",
    )
    cpsat = slice_text(
        script_text,
        "def resolver_cpsat(datos, cfg):",
        "# ══════════════════════════════════════════════════════════════════════════════\n# BLOQUE 4 — ALGORITMO GENÉTICO",
    )
    ga = slice_text(
        script_text,
        "def _cruce_ox(padre1, padre2):",
        "# ══════════════════════════════════════════════════════════════════════════════\n# BLOQUE 5 — ITERATED GREEDY",
    )
    ig = slice_text(
        script_text,
        "def resolver_ig(datos, cfg):",
        "# ══════════════════════════════════════════════════════════════════════════════\n# BLOQUE 6 — RESULTADOS, RPDs, SECUENCIAS Y SALIDA TXT",
    )
    reporting = slice_text(
        script_text,
        "_txt_buffer = []",
        "# ══════════════════════════════════════════════════════════════════════════════\n# EXTENSIONES",
    )
    extensions = slice_text(script_text, "# ── Checkpoint: carga progreso previo")

    cells = [
        md_cell(
            "# PPP notebook 02 — Benchmark execution\n\n"
            "This notebook mirrors the main execution workflow used in the project.\n\n"
            "It contains the cleaned code for:\n"
            "- the constructive evaluator used across methods;\n"
            "- the CP-SAT exact model;\n"
            "- the genetic algorithm;\n"
            "- the iterated-greedy metaheuristic;\n"
            "- the six benchmark extensions solved in the coursework.\n\n"
            "The original workbook is not published, but the code below is the public execution version of the project."
        ),
        md_cell(
            "## Imports and solver configuration\n\n"
            "This block defines the workbook path, the solver parameters, and the hyperparameters for the genetic algorithm and iterated greedy."
        ),
        code_cell(imports_cfg),
        md_cell(
            "## Loading the instance\n\n"
            "The project reads the generated benchmark sheets from the workbook and reconstructs all the arrays used by the exact and metaheuristic methods."
        ),
        code_cell(load_data),
        md_cell(
            "## Constructive greedy evaluator\n\n"
            "This is the core block reused by the metaheuristics. "
            "Given a permutation, it assigns jobs greedily while respecting the active constraints of each extension."
        ),
        code_cell(constructive),
        md_cell(
            "## CP-SAT formulation\n\n"
            "The exact approach uses OR-Tools CP-SAT with assignment variables, sequencing logic, precedence constraints and cumulative resources when required."
        ),
        code_cell(cpsat),
        md_cell(
            "## Genetic algorithm\n\n"
            "The GA works on job permutations, combining tournament selection, order crossover, swap/inversion mutation and elitism."
        ),
        code_cell(ga),
        md_cell(
            "## Iterated greedy\n\n"
            "This is the public execution version of the iterated-greedy procedure used in the project, with destroy-and-repair plus local reinsertion search."
        ),
        code_cell(ig),
        md_cell(
            "## Reporting and extension loop\n\n"
            "The final part of the workflow stores results, computes RPD values and executes the six benchmark extensions sequentially."
        ),
        code_cell(reporting),
        code_cell(extensions),
    ]
    return notebook(cells)


def write_notebook(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    NOTEBOOKS_DIR.mkdir(parents=True, exist_ok=True)
    script_01 = read_text(SCRIPT_01)
    script_02 = read_text(SCRIPT_02)

    nb_01 = build_instance_generation_notebook(script_01)
    nb_02 = build_benchmark_execution_notebook(script_02)

    write_notebook(NOTEBOOKS_DIR / "01_instance_generation_from_workbook.ipynb", nb_01)
    write_notebook(NOTEBOOKS_DIR / "02_benchmark_extensions_execution.ipynb", nb_02)


if __name__ == "__main__":
    main()
