import argparse
import nmap
import scapy.all as scapy
from netbiosss import NetBIOS

def scan_network(network):
    nm = nmap.PortScanner()
    nm.scan(network, arguments='-sn')
    hosts = nm.all_hosts()
    return hosts

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    return answered_list[0][1].hwsrc if answered_list else 'Unknown'

def get_netbios_name(ip):
    netbios = NetBIOS()
    name = netbios.queryName(ip)
    netbios.close()
    return name[0] if name else 'Unknown'

def print_hosts_info(hosts):
    for host in hosts:
        mac = get_mac(host)
        netbios_name = get_netbios_name(host)
        print(f'IP Address: {host}, MAC Address: {mac}, NetBIOS Name: {netbios_name}')

def main():
    parser = argparse.ArgumentParser(description="Network Scanner")
    parser.add_argument('network', type=str, help='The network to scan in CIDR notation (e.g., 192.168.1.0/24)')
    args = parser.parse_args()

    hosts = scan_network(args.network)
    print_hosts_info(hosts)

if __name__ == "__main__":
    main()
