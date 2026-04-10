from ipaddress import *
cnt = 0
for ip in ip_network('172.16.192.0/255.255.192.0', False):
    ip_2 = f'{ip:b}'
    if ip_2.count('1') % 5 != 0:
        cnt += 1
print(cnt)
