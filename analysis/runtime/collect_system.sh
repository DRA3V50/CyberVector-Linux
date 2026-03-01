echo ""
echo "Running Services:" >> $OUTPUT
systemctl list-units --type=service --state=running >> $OUTPUT

echo ""
echo "SUID Files:" >> $OUTPUT
find / -perm -4000 2>/dev/null >> $OUTPUT

echo ""
echo "Cron Jobs:" >> $OUTPUT
ls -la /etc/cron* >> $OUTPUT 2>/dev/null

echo ""
echo "SSH Configuration Snippet:" >> $OUTPUT
grep -E "PermitRootLogin|PasswordAuthentication" /etc/ssh/sshd_config 2>/dev/null >> $OUTPUT
