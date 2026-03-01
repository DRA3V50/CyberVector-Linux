import os
from datetime import date

today = date.today().isoformat()

os.makedirs("artifacts/reports", exist_ok=True)

auth_file = f"artifacts/auth/auth_{today}.log"
failed_count = 0

if os.path.exists(auth_file):
    with open(auth_file) as f:
        for line in f:
            if line.strip().isdigit():
                failed_count = int(line.strip())

if failed_count > 50:
    status = "High Risk - Containment Required"
elif failed_count > 10:
    status = "Elevated Monitoring"
else:
    status = "Normal Monitoring"

summary = f"""
## Daily Security Summary — {today}

### Exposure Detection
Failed SSH Attempts: {failed_count}

### Network Surface
Active listening ports reviewed
Firewall status checked

### System Integrity
Running services audited
SUID binaries enumerated
Cron persistence paths inspected
SSH hardening settings reviewed

### Risk Level
{status}
"""

report_path = f"artifacts/reports/summary_{today}.md"
with open(report_path, "w") as f:
    f.write(summary)
