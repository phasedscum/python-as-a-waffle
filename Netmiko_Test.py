
from netmiko import ConnectHandler
import os
import errno
import datetime
import time
from IPy import IP
from colorama import init
import sys

timestamp = time.strftime(".%H%M%S")

print('\033[31m' + 'This is a Python scrip to generate typical "Show" commands for Cisco IOS and IOS XE devices,')
print('normal device config generation time still applies.')
print('v0.1 Beta')
init(wrap=False)

try:
    ipaddr = input('Please enter IP Address : ')
    IP(ipaddr)
except ValueError:
    print('Invalid Ip')
    sys.exit(1)

username = input('Please enter username : ')
password = input('Please enter device password : ')
secret = input('Please enter secret : ')
cisco_devices = {
    'device_type': 'cisco_ios',
    'ip': ipaddr,
    'username': username,
    'password': password,
}
if not os.path.exists("C:/sshoutput/"):
    os.mkdir("C:/sshoutput/")

"""filename = ipaddr + str(timestamp) + '.txt'"""
print('Generating....' )

net_connect = ConnectHandler(**cisco_devices)

output = net_connect.send_command('show ip int brief')
print(output, file=open(ipaddr + str(timestamp) + ".txt", "a"))
print(output)
sys.stdout = orig_outp
f.close()
