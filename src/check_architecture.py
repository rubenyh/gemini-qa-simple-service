from pathlib import Path
import re
import sys

# read container aliases from the architectue contract
diagram = (Path(__file__).resolve().parent.parent/ "README.md").read_text(encoding="utf-8")
aliases = re.findall(r"^\s*Container\(([^,]+),", diagram, re.MULTILINE)

# map each internal alias to the python module it names
missing = [f"{alias}.py" for alias in aliases if not (Path(__file__).resolve().parent / f"{alias}.py").exists()]

if missing:
    print("Architecture drift detected")
    print(f"Missing modules: {', '.join(missing)}")
    sys.exit(1)

print("Architecture matches the diagram")
