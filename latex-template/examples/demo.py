"""Teaching example only: exact formulas, not competition measurements."""
import csv
from pathlib import Path


def objectives(x, radius=0.1):
    if not 0 <= x <= 4 or radius < 0:
        raise ValueError("Require x in [0,4] and a nonnegative radius")
    return (x - 2) ** 2, (abs(x - 2) + radius) ** 2


def main():
    out = Path(__file__).resolve().parents[1] / "generated"
    out.mkdir(exist_ok=True)
    rows = [(name, x, *objectives(x))
            for name, x in [("baseline", 1.0), ("analytic", 2.0)]]
    with (out / "demo.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["method", "x", "nominal", "worst_case"])
        writer.writerows(rows)
    lines = [r"\begin{table}[htbp]", r"\centering",
             r"\caption{Teaching example: exact objective values}",
             r"\label{tab:demo}", r"\begin{tabular}{lrrr}",
             r"\toprule Method & $x$ & $J(x)$ & $J_{\mathrm{rob}}(x)$ \\",
             r"\midrule"]
    for name, x, nominal, worst in rows:
        lines.append(f"{name} & {x:.1f} & {nominal:.2f} & {worst:.2f}" + r" \\")
    lines += [r"\bottomrule", r"\end{tabular}", r"\end{table}"]
    (out / "demo-table.tex").write_text("\n".join(lines) + "\n",
                                      encoding="utf-8")


if __name__ == "__main__":
    main()
