import scapy
import keyboard

# Define a callback function to process packets
def packet_callback(packet):
    print(packet.summary())

# Function to start sniffing packets
def start_sniffing():
    print("Press 'q' to stop sniffing...")
    while True:
      #Note only capture a packet and print before we grab the next, can also specify filter type.  filter='tcp'
      #need to link these settings with a config file.
        sniff(iface="eth0", prn=packet_callback, count=1)
        if keyboard.is_pressed('q'):
            print("Sniffing stopped.")
            break

# Start the sniffing process
start_sniffing()
