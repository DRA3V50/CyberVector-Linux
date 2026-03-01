echo ""
echo "Top Failed IP Sources:" >> $OUTPUT
grep "Failed password" /var/log/auth.log 2>/dev/null | \
awk '{print $(NF-3)}' | sort | uniq -c | sort -nr | head >> $OUTPUT
