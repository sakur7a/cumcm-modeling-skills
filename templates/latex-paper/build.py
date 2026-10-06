"""Portable offline build; requires Python 3.9+ and XeLaTeX on PATH."""
import re
import shutil
import subprocess
import sys
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent
    engine = shutil.which("xelatex")
    if not engine:
        raise SystemExit("XeLaTeX not found. Install a TeX distribution with CTeX/Fandol.")
    subprocess.run([sys.executable, str(root / "examples/demo.py")], check=True)
    out = root / "build"
    out.mkdir(exist_ok=True)
    for name in ["main", "ai-usage"]:
        for run in range(2):
            result = subprocess.run(
                [engine, "-interaction=nonstopmode", "-halt-on-error",
                 "-file-line-error", "-output-directory=build", name + ".tex"],
                cwd=root, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            (out / f"{name}-pass{run + 1}.txt").write_bytes(result.stdout)
            if result.returncode:
                raise SystemExit(f"Compilation failed: build/{name}-pass{run + 1}.txt")
        log = (out / (name + ".log")).read_text(encoding="utf-8", errors="replace")
        problems = re.findall(
            r"[^\n]*(?:undefined|Missing character|Overfull|Rerun to get)[^\n]*", log)
        if problems:
            raise SystemExit("Inspect LaTeX diagnostics:\n" + "\n".join(problems))
        print("Built:", out / (name + ".pdf"))


if __name__ == "__main__":
    main()
