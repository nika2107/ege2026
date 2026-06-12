from ipaddress import *

for mask in range(32, 0, -1):
    net = ip_network(f'121.171.5.70/{mask}', 0)
    if ip_address('121.171.5.107') in net:
        print(net.num_addresses)
        break