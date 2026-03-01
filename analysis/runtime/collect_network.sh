#!/bin/bash

mkdir -p artifacts/network

OUTPUT="artifacts/network/network_$(date +%F).log"

echo "[Phase II - Surface Exposure Mapping]" > $OUTPUT
echo "Collection Time: $(date)" >> $OUTPUT
echo "-----------------------------------" >> $OUTPUT

ss -tulnp >> $OUTPUT
