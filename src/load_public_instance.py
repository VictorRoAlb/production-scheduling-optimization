from __future__ import annotations

import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
INSTANCE_DIR = BASE_DIR / "examples" / "instance_csv"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def load_public_instance(instance_dir: Path = INSTANCE_DIR) -> dict[str, object]:
    release_dates = read_rows(instance_dir / "release_dates.csv")
    due_dates = read_rows(instance_dir / "due_dates.csv")
    weights = read_rows(instance_dir / "pesos.csv")
    precedences = read_rows(instance_dir / "precedencias.csv")
    resources = read_rows(instance_dir / "recursos.csv")
    setup_files = sorted(instance_dir.glob("setups_M*.csv"))

    capacity = None
    if resources:
        capacity = next((row["H_total"] for row in resources if row.get("H_total")), None)

    return {
        "num_jobs": len(release_dates),
        "num_setup_matrices": len(setup_files),
        "num_precedences": len(precedences),
        "resource_capacity": int(capacity) if capacity else None,
        "files": {
            "release_dates": "release_dates.csv",
            "due_dates": "due_dates.csv",
            "weights": "pesos.csv",
            "precedences": "precedencias.csv",
            "resources": "recursos.csv",
            "setups": [path.name for path in setup_files],
        },
    }


if __name__ == "__main__":
    summary = load_public_instance()
    print("Public PPP instance summary")
    print(f"Jobs: {summary['num_jobs']}")
    print(f"Setup matrices: {summary['num_setup_matrices']}")
    print(f"Precedence pairs: {summary['num_precedences']}")
    print(f"Shared resource capacity: {summary['resource_capacity']}")

