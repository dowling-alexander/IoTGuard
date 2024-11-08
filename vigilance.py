from scapy.all import sniff, wrpcap

# Define a function to print packets
def packet_print(packet):
    #this is a basic summary, look at how to provide more details back to the user with packet.show and packet.hexdump.
    print(packet.summary())

# Define a function to process packets
def packet_callback(packet):
    captured_packets.append(packet)

# Function to start sniffing packets
def start_sniffing(iface_input):
      #Note only capture a packet and print before we grab the next, can also specify filter type.  filter='tcp'
      #need to link these settings with a config file.
        sniff(iface=iface_input, prn=packet_print, count=1)

#Function to start logging packets.
def start_logging(iface_input, filename):
    full_filename=f"{filename}.pcap"
    sniff(iface=iface_input, prn=packet_callback)
    wrpcap(full_filename, captured_packets, append=True)
    print(f"Packets logged to {full_filename}")




