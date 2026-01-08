from ipaddress import *

net = ip_network('44.195.57.194/255.255.255.248', 0)
print(net[1])
print(net[-2])