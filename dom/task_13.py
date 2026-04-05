from ipaddress import *

cnt = 0

for ip in ip_network('172.16.96.0/255.255.224.0', 0):
    ip_2 = f'{ip:b}'
    if ip_2.count('1') % 2 == 0:
        cnt += 1
print(cnt)