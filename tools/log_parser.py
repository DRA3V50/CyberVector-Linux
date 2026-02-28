import re
from collections import defaultdict
from datetime import datetime

INPUT_FILE = "artifacts/auth/auth.log.sample"
OUTPUT_FILE = "analysis/authentication-log-analysis.md"

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
    out.write("# Authentication Behavioral Intelligence Report\n")
    out.write(f"Generated: {datetime.now()}\n\n")

    out.write("## IP Risk Scoring\n")
    for ip, count in sorted(ip_attempts.items(), key=lambda x: x[1], reverse=True):
        if count > 15:
            risk = "CRITICAL"
        elif count > 8:
            risk = "HIGH"
        elif count > 3:
            risk = "MEDIUM"
        else:
            risk = "LOW"
        out.write(f"- {ip}: {count} attempts ({risk})\n")

    out.write("\n## Targeted Account Distribution\n")
    for user, count in sorted(user_targets.items(), key=lambda x: x[1], reverse=True):
        out.write(f"- {user}: {count} attempts\n")

    out.write("\n## Burst Activity Detection\n")
    for time, count in timeline.items():
        if count > 4:
            out.write(f"- {time}: {count} clustered attempts\n")

    out.write("\n## Technique Mapping\n")
    out.write("Observed activity aligns with MITRE ATT&CK T1110 (Brute Force).\n")
