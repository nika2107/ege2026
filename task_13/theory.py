from ipaddress import *

ip = ip_address('16.16.0.0')

net = ip_network('128.192.0.1/255.255.255.240', False)

# Кол-во ip-адресов в текущей сети
num_address = net.num_addresses

# Широковещательный. Не может быть задан для устройств
broadcast_address = net.broadcast_address

# Адрес сети. Не может быть задан для устройств
network_address = net.network_address

# Список всех хостов / узлов / ip-aдресов для устройств
hosts = net.hosts()

# Возвращает маску сети
mask = net.netmask


print(broadcast_address)
print(f'{int(broadcast_address):032b}')
print(network_address)
print(f'{int(network_address):032b}')



print(num_address)
for i in net:
    print(f'{int(ip):032b}')


#Варианты значений в маске
# 255.255.A.0
#11111111.11111111.00000000.000000000