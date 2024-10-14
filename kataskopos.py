import psutil

def get_active_interfaces():
    interfaces = psutil.net_if_addrs()
    active_interfaces = [iface for iface, addrs in interfaces.items() if addrs]
    return active_interfaces

active_interfaces = get_active_interfaces()
print(f"Active network interfaces: {active_interfaces}")
