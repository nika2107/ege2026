from ipaddress import *

for A in range(256):
    net = ip_network(f'192.214.{A}.184/255.255.255.224', False)

    if all(bin(int(addr)).count('1') > 15 for addr in net):
        print(A)
        break
