#was in a latin mood for these naming conventions. Will come back to this. use scapy to record files to a .pcap
from scapy.all import sniff, wrpcap

def log_packets():
  packets =sniff(count=10)
  wrpcap('packets.pcap', packets)
