from ipaddress import *

net = ip_network('158.214.121.40/255.255.255.224',0)
print(net[-2])
print(146+191+255+254)