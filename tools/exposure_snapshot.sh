#!/bin/bash

OUTPUT="validation/exposure-snapshot.md"

echo "# Host Exposure Risk Assessment" > $OUTPUT
echo "Generated on: $(date)" >> $OUTPUT
echo "" >> $OUTPUT

echo "## Listening Ports" >> $OUTPUT
ss -tulnp >> $OUTPUT
echo "" >> $OUTPUT

echo "## SSH Configuration Risk Analysis" >> $OUTPUT

if grep -q "^PasswordAuthentication yes" /etc/ssh/sshd_config 2>/dev/null; then
    echo "- PasswordAuthentication: ENABLED (HIGH RISK)" >> $OUTPUT
else
    echo "- PasswordAuthentication: Disabled" >> $OUTPUT
fi

if grep -q "^PermitRootLogin yes" /etc/ssh/sshd_config 2>/dev/null; then
    echo "- Root Login: ENABLED (CRITICAL RISK)" >> $OUTPUT
else
    echo "- Root Login: Disabled" >> $OUTPUT
fi
