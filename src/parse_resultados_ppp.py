from __future__ import annotations

import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
RESULTS_PATH = BASE_DIR / "results" / "resultados_ppp_public.txt"


def parse_extensions(text: str) -> list[dict[str, object]]:
    normalized = text.replace("\r\n", "\n")
    pattern = re.compile(r"EXTENSION\s+(\d+)\s+--\s+(.+?)\n(.*?)(?=\n=+\n\s*EXTENSION|\Z)", re.S)
    row_pattern = re.compile(
        r"^\s*(IG|Genetico|CP-SAT)\s+([A-Za-z]+)\s+([0-9.]+)\s+([0-9.]+)(?:\s+<<\s+MEJOR)?\s*$",
        re.M,
    )
    parsed: list[dict[str, object]] = []
    for match in pattern.finditer(normalized):
        extension_id, description, block = match.groups()
        methods = []
        for method, status, objective, runtime in row_pattern.findall(block):
            methods.append(
                {
                    "method": method,
                    "status": status,
                    "objective": float(objective),
                    "runtime_seconds": float(runtime),
                }
            )
        parsed.append(
            {
                "extension": int(extension_id),
                "description": description.strip(),
                "methods": methods,
            }
        )
    return parsed


if __name__ == "__main__":
    text = RESULTS_PATH.read_text(encoding="utf-8", errors="ignore")
    extensions = parse_extensions(text)
    if not extensions:
        raise SystemExit("No extensions could be parsed from resultados_ppp_public.txt")
    for item in extensions:
        print(f"Extension {item['extension']}: {item['description']}")
        for method in item["methods"]:
            print(
                f"  - {method['method']}: objective={method['objective']:.2f}, "
                f"time={method['runtime_seconds']:.2f}s, status={method['status']}"
            )
