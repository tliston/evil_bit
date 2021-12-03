#!/usr/bin/env python3
# this python script MUST be run as root

# also, once this is running, it is necessary to run the
# following iptables command designating the appropriate device:
# iptables -A OUTPUT -o <device> -p IP -j NFQUEUE --queue-num 3514

from scapy.all import *
from netfilterqueue import NetfilterQueue

def doIt(packet):
	scapypkt = IP(packet.get_payload())
	scapypkt[IP].flags |= 4
	del scapypkt[IP].chksum
	packet.set_payload(bytes(scapypkt))
	packet.accept()

# bind the callback function to the queue
nfqueue = NetfilterQueue()
nfqueue.bind(3514, doIt)

try:
	nfqueue.run()
except KeyboardInterrupt:
	pass
