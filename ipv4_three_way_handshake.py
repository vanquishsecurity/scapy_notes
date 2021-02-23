from scapy.all import *

sport = random.randint(1024,65535)
dport = XXXXX

# SYN
ip=IP(src='X.X.X.X',dst='X.X.X.X')
SYN=TCP(sport=sport,dport=XXXXX,flags='S',seq=1000)
SYNACK=sr1(ip/SYN)

# SYN-ACK
ACK=TCP(sport=sport, dport=XXXXX, flags='A', seq=SYNACK.ack + 1, ack=SYNACK.seq + 1)

send(ip/ACK, count=5)
