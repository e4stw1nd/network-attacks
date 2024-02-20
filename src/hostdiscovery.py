from scapy.all import *
from scapy.layers.inet import IP,ICMP
def hostdiscovery(ip):
    pkt=IP(dst=ip)/ICMP()
    reply=sr1(pkt,timeout=5,verbose=0)
    if reply is None:
        print("Host:",ip,"is offline.")
        return 0
    else:
        print("Host:",ip,"is up.")
        return 1
#hostdiscovery("127.0.0.1")