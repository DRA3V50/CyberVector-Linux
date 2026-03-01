# Host Exposure Risk Assessment
Generated on: Sun Mar  1 14:14:53 UTC 2026

## Listening Ports
Netid State  Recv-Q Send-Q  Local Address:Port Peer Address:PortProcess
udp   UNCONN 0      0          127.0.0.54:53        0.0.0.0:*          
udp   UNCONN 0      0       127.0.0.53%lo:53        0.0.0.0:*          
udp   UNCONN 0      0      10.1.0.42%eth0:68        0.0.0.0:*          
udp   UNCONN 0      0           127.0.0.1:323       0.0.0.0:*          
udp   UNCONN 0      0               [::1]:323          [::]:*          
tcp   LISTEN 0      4096       127.0.0.54:53        0.0.0.0:*          
tcp   LISTEN 0      4096    127.0.0.53%lo:53        0.0.0.0:*          
tcp   LISTEN 0      4096          0.0.0.0:22        0.0.0.0:*          
tcp   LISTEN 0      4096             [::]:22           [::]:*          

## SSH Configuration Risk Analysis
- PasswordAuthentication: Disabled
- Root Login: Disabled
