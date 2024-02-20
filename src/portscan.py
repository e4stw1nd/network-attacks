from scapy.all import *
from scapy.layers.inet import IP,TCP
import hostdiscovery
import sys
def portscan(ip):
    if sys.argv[1]=="0":
        print("Skipping Host Discovery.")
    else:
        print("Checking for host discovery:")
        up=hostdiscovery.hostdiscovery(ip)
        if up==0:
            print("Quitting...")
            exit()

    for i in range(1,65536):
        pkt=IP(dst=ip)/TCP(sport=80,dport=i,flags='S')
        recv=sr1(pkt,verbose=False,timeout=0.5)
        if recv.haslayer(TCP) and recv.getlayer(TCP).flags==18:
            print(i,"port is open on target",ip)
        send(IP(dst=ip)/TCP(sport=80,dport=i,flags='R'))
