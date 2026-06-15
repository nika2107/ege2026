from ipaddress import *

ip = ip_address('153.202.16.37')

for mask in range(33):
    net = ip_network(f'{ip}/{mask}', 0)
    if str(net.network_address) == '153.202.16.32':
        x = int(net.netmask)
        print((x // 256) % 256 + x % 256)