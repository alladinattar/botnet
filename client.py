from scapy.all import *


packets = sniff(filter = "icmp", count = 100,timeout = 5, iface = "enp0s3")

for pkt in packets:
  
    if pkt[ICMP].type != 8:
        continue
    
    a, b = divmod(pkt[IP].id, 0x100)
    print(chr(a))
    print(chr(b))
