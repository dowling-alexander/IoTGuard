#was in a latin mood for these naming conventions. Will come back to this. use scapy to record files to a .pcap
from scapy.all import sniff, wrpcap

def log_packets(filename, packets):
  full_filename=f"{filename}.pcap"
  wrpcap(full_filename, packets,append=true)
  
