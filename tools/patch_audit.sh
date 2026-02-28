#!/bin/bash

OUTPUT="patch-management/ubuntu-security-update-log.md"

echo "# Patch Intelligence Report" > $OUTPUT
echo "Generated on: $(date)" >> $OUTPUT
echo "" >> $OUTPUT

UPDATES=$(apt list --upgradable 2>/dev/null)

echo "## Pending Updates" >> $OUTPUT
echo "$UPDATES" >> $OUTPUT
echo "" >> $OUTPUT

echo "## Kernel Version" >> $OUTPUT
uname -r >> $OUTPUT
echo "" >> $OUTPUT

echo "## Exploitability Analysis" >> $OUTPUT

if echo "$UPDATES" | grep -q openssh; then
    echo "- OpenSSH update pending. Remote compromise risk elevated." >> $OUTPUT
fi

if echo "$UPDATES" | grep -q sudo; then
    echo "- Sudo update pending. Privilege escalation risk present." >> $OUTPUT
fi
