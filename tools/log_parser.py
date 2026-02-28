import re
from collections import defaultdict
from datetime import datetime

INPUT_FILE = "artifacts/auth/auth.log.sample"
OUTPUT_FILE = "analysis/daily-auth-summary.md"

failed_pattern = re.compile(r"Failed password for (invalid user )?(\w+) from ([\d\.]+)")
time_pattern = re.compile(r"^(\w+\s+\d+\s+\d+:\d+:\d+)")

ip_attempts = defaultdict(int)
user_targets = defaultdict(int)
timeline = defaultdict(int)

try:
    with open(INPUT_FILE, "r") as f:
        for line in f:
            if "Failed password" in line:
                match = failed_pattern.search(line)
                time_match = time_pattern.search(line)

                if match:
                    user = match.group(2)
                    ip = match.group(3)
                    ip_attempts[ip] += 1
                    user_targets[user] += 1

                if time_match:
                    timeline[time_match.group(1)] += 1

except FileNotFoundError:
    pass

with open(OUTPUT_FILE, "w") as out:
    out.write("# Authentication Behavioral Analysis\n")
    out.write(f"Generated: {datetime.now()}\n\n")

    out.write("## Brute Force Indicators\n")
    for ip, count in sorted(ip_attempts.items(), key=lambda x: x[1], reverse=True):
        risk = "HIGH" if count > 10 else "MEDIUM" if count > 5 else "LOW"
        out.write(f"- {ip}: {count} attempts ({risk})\n")

    out.write("\n## Targeted Accounts\n")
    for user, count in sorted(user_targets.items(), key=lambda x: x[1], reverse=True):
        out.write(f"- {user}: {count} attempts\n")

    out.write("\n## Attack Density Timeline\n")
    for time, count in timeline.items():
        if count > 3:
            out.write(f"- {time}: {count} clustered attempts\n")

    out.write("\n## Defensive Control Assessment\n")
    if any(c > 10 for c in ip_attempts.values()):
        out.write("Sustained brute-force activity detected. Fail2ban threshold tuning recommended.\n")
    else:
        out.write("No sustained brute-force patterns detected.\n")
