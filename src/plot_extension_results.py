from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from parse_resultados_ppp import RESULTS_PATH, parse_extensions


BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_PATH = BASE_DIR / "figures" / "extension_method_comparison.png"

METHOD_ORDER = ["IG", "Genetico", "CP-SAT"]
METHOD_LABELS = {
    "IG": "Iterated Greedy",
    "Genetico": "Genetic algorithm",
    "CP-SAT": "CP-SAT",
}
COLORS = {
    "IG": "#245a86",
    "Genetico": "#5f8f66",
    "CP-SAT": "#c8744a",
}


def main() -> None:
    text = RESULTS_PATH.read_text(encoding="utf-8", errors="ignore")
    extensions = parse_extensions(text)
    if not extensions:
        raise SystemExit("No extensions could be parsed from resultados_ppp_public.txt")

    extension_labels = [f"E{item['extension']}" for item in extensions]
    x = np.arange(len(extensions))
    width = 0.24

    fig, axes = plt.subplots(
        2,
        1,
        figsize=(12.5, 9.2),
        constrained_layout=True,
        facecolor="white",
    )

    for offset, method in zip((-width, 0, width), METHOD_ORDER):
        objectives = []
        runtimes = []
        for item in extensions:
            method_row = next(row for row in item["methods"] if row["method"] == method)
            objectives.append(method_row["objective"])
            runtimes.append(method_row["runtime_seconds"])

        axes[0].bar(
            x + offset,
            objectives,
            width=width,
            color=COLORS[method],
            label=METHOD_LABELS[method],
            alpha=0.94,
        )
        axes[1].bar(
            x + offset,
            runtimes,
            width=width,
            color=COLORS[method],
            alpha=0.94,
        )

    axes[0].set_title("Objective value by benchmark extension", fontsize=15, weight="bold", pad=10)
    axes[0].set_ylabel("Best objective", fontsize=11)
    axes[0].set_xticks(x, extension_labels)
    axes[0].grid(axis="y", linestyle="--", alpha=0.25)
    axes[0].set_axisbelow(True)

    axes[1].set_title("Runtime by benchmark extension", fontsize=15, weight="bold", pad=10)
    axes[1].set_ylabel("Runtime (s)", fontsize=11)
    axes[1].set_xticks(x, extension_labels)
    axes[1].set_xlabel("PPP extension", fontsize=11)
    axes[1].grid(axis="y", linestyle="--", alpha=0.25)
    axes[1].set_axisbelow(True)
    axes[1].set_yscale("log")

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=3, frameon=False, bbox_to_anchor=(0.5, 1.02))
    fig.suptitle(
        "Production scheduling benchmark: method comparison across six extensions",
        fontsize=18,
        weight="bold",
        y=1.05,
    )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_PATH, dpi=220, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
