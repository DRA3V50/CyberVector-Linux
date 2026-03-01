#!/bin/bash

mkdir -p artifacts/auth

OUTPUT="artifacts/auth/auth_$(date +%F).log"

echo "[Phase I - Exposure Detection]" > $OUTPUT
echo "Collection Time: $(date)" >> $OUTPUT
echo "-----------------------------------" >> $OUTPUT

if [ -f /var/log/auth.log ]; then
    grep "Failed password" /var/log/auth.log >> $OUTPUT
    echo "" >> $OUTPUT
    echo "Total Failed Attempts:" >> $OUTPUT
    grep -c "Failed password" /var/log/auth.log >> $OUTPUT
else
    echo "auth.log not found on this system." >> $OUTPUT
fi
