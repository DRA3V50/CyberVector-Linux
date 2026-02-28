#!/bin/bash

INPUT="artifacts/auth/auth.log.sample"
OUTPUT="analysis/brute-force-detection.md"

echo "# Brute Force Detection Summary" > $OUTPUT
echo "Generated on: $(date)" >> $OUTPUT
echo "" >> $OUTPUT

if [ ! -f "$INPUT" ]; then
    echo "No artifact log available." >> $OUTPUT
    exit 0
fi

IPS=$(grep "Failed password" $INPUT | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr)

echo "## IP Attempt Counts" >> $OUTPUT
echo "$IPS" >> $OUTPUT
echo "" >> $OUTPUT

CRITICAL=$(echo "$IPS" | awk '$1 > 15')

if [ -n "$CRITICAL" ]; then
    echo "## Critical Brute Force Activity Detected" >> $OUTPUT
    echo "$CRITICAL" >> $OUTPUT
else
    echo "No critical brute force clusters detected." >> $OUTPUT
fi
