#!/bin/bash

mkdir -p artifacts/system

OUTPUT="artifacts/system/system_$(date +%F).log"

echo "[Phase III - Host Immunization Status]" > $OUTPUT
echo "Collection Time: $(date)" >> $OUTPUT
echo "-----------------------------------" >> $OUTPUT

apt list --upgradable 2>/dev/null >> $OUTPUT
