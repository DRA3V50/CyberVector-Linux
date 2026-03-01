import os
from datetime import date

today = date.today().isoformat()
report_path = f"artifacts/reports/summary_{today}.md"

os.makedirs("artifacts/reports", exist_ok=True)

failed_count = 0
auth_file = f"artifacts/auth/auth_{today}.log"

if os.path.exists(auth_file):
    with open(auth_file) as f:
        for line in f:
            if line.strip().isdigit():
                failed_count = int(line.strip())

summary = f"""
## Daily Containment Report — {today}

**Phase I – Exposure Events**
- Failed SSH Attempts: {failed_count}

**Phase II – Surface Mapping**
- Network scan executed

**Phase III – Immunization Check**
- Patch review completed

Containment Status: Monitoring
"""

with open(report_path, "w") as f:
    f.write(summary)

# Inject into README
with open("README.md", "r") as f:
    readme = f.read()

start_marker = "<!-- CVX-REPORT-START -->"
end_marker = "<!-- CVX-REPORT-END -->"

if start_marker in readme and end_marker in readme:
    before = readme.split(start_marker)[0]
    after = readme.split(end_marker)[1]
    new_readme = before + start_marker + summary + end_marker + after
    with open("README.md", "w") as f:
        f.write(new_readme)
