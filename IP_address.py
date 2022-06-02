import re

N = int(input())

ip_add = [input() for _ in range(N)]

p6 = r'^([a-f0-9]{0,4}:){7}[a-f0-9]{0,4}$'
p4 = r'^(([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'




for ip in ip_add:
    if re.search(p6, ip):
        print('IPv6')
    elif re.search(p4,ip):
        print('IPv4')
    else:
        print('Neither')
