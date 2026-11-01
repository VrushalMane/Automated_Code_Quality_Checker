
import subprocess
from pathlib import Path

files = ["app.py", "test_app.py"]

result = subprocess.run(
    ["python", "-m", "flake8", *files],
    capture_output=True,
    text=True
)

violations = result.stdout.strip().splitlines()
violations = [line for line in violations if line]

total_violations = len(violations)

if total_violations == 0:
    status = "PASSED"
else:
    status = "FAILED"

report = f"""
AUTOMATED CODE QUALITY REPORT
=============================

Files Checked: {len(files)}
Total Violations: {total_violations}
Code Quality Status: {status}

Violations:
"""

if violations:
    report += "\n".join(violations)
else:
    report += "No code quality issues found."

Path("code-quality-report.txt").write_text(report)

print(report)
