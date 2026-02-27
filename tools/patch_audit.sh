#!/bin/bash

OUTPUT="patch-management/ubuntu-security-update-log.md"

echo "# Ubuntu Security Update Log" > $OUTPUT
echo "Generated on: $(date)" >> $OUTPUT
echo "" >> $OUTPUT

echo "## Upgradable Packages" >> $OUTPUT
apt list --upgradable 2>/dev/null >> $OUTPUT
