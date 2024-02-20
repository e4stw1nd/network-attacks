from scapy.all import *
from scapy.layers.inet import Ether,ARP
def mac_resolv(ip):
    arp= Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=1, pdst=ip)
    mac= srp(arp, timeout=5)[0][0][1].hwsrc
    return mac