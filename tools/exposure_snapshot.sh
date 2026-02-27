#!/bin/bash

OUTPUT="validation/exposure-snapshot.md"

echo "# Exposure Snapshot" > $OUTPUT
echo "Generated on: $(date)" >> $OUTPUT
echo "" >> $OUTPUT

echo "## Active Listening Ports" >> $OUTPUT
ss -tulnp >> $OUTPUT
