from scapy.all import sniff


# Define a callback function to process packets
def packet_callback(packet):
    #this is a basic summary, look at how to provide more details back to the user with packet.show and packet.hexdump.
    print(packet.summary())

# Function to start sniffing packets
def start_sniffing(iface_input):
      #Note only capture a packet and print before we grab the next, can also specify filter type.  filter='tcp'
      #need to link these settings with a config file.
    #while True:
        sniff(iface=iface_input, prn=packet_callback, count=1)




