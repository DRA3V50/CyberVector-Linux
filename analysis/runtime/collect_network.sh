echo ""
echo "Listening Ports:" >> $OUTPUT
ss -tulnp >> $OUTPUT 2>/dev/null

echo ""
echo "Firewall Status:" >> $OUTPUT
sudo ufw status >> $OUTPUT 2>/dev/null
