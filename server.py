from scapy.all import *

payload = ord("A") * 0x100 + ord("B")
pkt = IP(src="10.0.0.1", dst="10.0.0.1",id = payload) / ICMP(type = 8)

sr1(pkt)
