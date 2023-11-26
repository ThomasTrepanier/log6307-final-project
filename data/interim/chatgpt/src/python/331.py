def print_hosts_info(hosts):
    for host in hosts:
        mac = get_mac(host)
        host_name = get_hostname(host)
        try:
            manufacturer = get_manufacturer(mac)
        except ValueError:
            manufacturer = 'Unknown'
        print(f'IP Address: {host}, MAC Address: {mac}, Host Name: {host_name}, Manufacturer: {manufacturer}')
