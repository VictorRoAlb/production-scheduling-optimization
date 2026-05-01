from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"


ROWS = [
    ("E0", "R || Cmax", "Iterated Greedy", "168.00", "78.86"),
    ("E1", "R | rj | Cmax", "Iterated Greedy", "169.00", "83.45"),
    ("E2", "R | rj, sijk | Cmax", "Iterated Greedy", "195.00", "94.65"),
    ("E3", "R | rj, sijk, prec | Cmax", "Iterated Greedy", "197.00", "214.80"),
    ("E4", "R | rj, sijk, prec, res | Cmax", "Iterated Greedy", "199.00", "2191.15"),
    ("E5", "R | rj, sijk, prec, res | sum(wjTj)", "Iterated Greedy", "3060.00", "5640.78"),
]


def main() -> None:
    fig, ax = plt.subplots(figsize=(15.6, 4.9), facecolor="white")
    ax.axis("off")

    col_labels = ["Extension", "Formulation", "Best method", "Best objective", "Best time (s)"]
    table = ax.table(
        cellText=[list(row) for row in ROWS],
        colLabels=col_labels,
        cellLoc="center",
        loc="center",
        colWidths=[0.08, 0.36, 0.20, 0.16, 0.14],
    )

    table.auto_set_font_size(False)
    table.set_fontsize(10.5)
    table.scale(1, 1.9)

    header_color = "#DCE8F1"
    accent_color = "#EDF4E7"
    border_color = "#C8D3DE"

    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor(border_color)
        if row == 0:
            cell.set_facecolor(header_color)
            cell.set_text_props(weight="bold", color="#213243")
        else:
            if col == 2:
                cell.set_facecolor(accent_color)
                cell.set_text_props(weight="bold", color="#29492C")
            else:
                cell.set_facecolor("white")

    fig.suptitle("Final benchmark results by extension", fontsize=20, fontweight="bold", y=0.96)
    fig.text(
        0.5,
        0.07,
        "Each row reports the strongest final method for one benchmark extension in the PPP project.",
        ha="center",
        fontsize=10.4,
        color="#555555",
    )
    fig.subplots_adjust(left=0.02, right=0.98, top=0.83, bottom=0.12)
    out_path = FIGURES / "final_results_table.png"
    fig.savefig(out_path, dpi=320, bbox_inches="tight")
    plt.close(fig)
    print(out_path)


if __name__ == "__main__":
    main()
