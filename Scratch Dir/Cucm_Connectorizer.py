#!/usr/bin/env python
#from xcelip import iprecs
from netmiko.linux import LinuxSSH
from netmiko import ConnectHandler
import os
import errno
import datetime
import time
from IPy import IP
from colorama import init,Fore, Back, Style
import sys
import getpass

timestamp = time.strftime(".%H%M%S")

__author__ = "John Ng"
__copyright__ = "Copyright 2018, John Ng"
__license__ = "MIT License"
__version__ = "v0. Beta"
__status__ = "Prototype"
init(strip=False)
print('\033[91m' + 'This is a Python scrip to generate pre-defined commands for Cisco UC OS devices only,')
print('\033[91m' + 'Files will be generated and saved in the same folder as this app in accordance of IP & Timestamp')
print('\033[91m' + 'Normal device config generation time and resources consumption still applies.')
print(Fore.CYAN + Style.BRIGHT + '[v0.4 Beta]')
init(wrap=False)
print('\033[30m')

cleanslate = sys.stdout
try:
    ipaddr = input('Please enter IP Address : ') # Manual IP Prompt
    #ipaddr = iprecs # Pull data through excel file from xcelip module
    IP(ipaddr)
except ValueError:
    print('Invalid Ip Detected')
    sys.exit(1)

username = input('Please enter username : ')
password = getpass.getpass(prompt='Please enter device password : ')
#password = input('Please enter device password : ')
cisco_devices = {
    'device_type': 'linux',
    'ip': ipaddr,
    'username': username,
    'password': password,
    'global_delay_factor': 7,
}

#if not os.path.exists("C:/sshoutput/"): # Test block for cuscomized target direcotory
    #os.mkdir("C:/sshoutput/")
#path = 'C:/sshoutput/'

"""filename = ipaddr + str(timestamp) + '.txt'"""
print('Generating.....' )
net_connect = ConnectHandler(**cisco_devices)

fileout = open(ipaddr + str(timestamp) + ".txt", "a")
sys.stdout = fileout
ucos_commands = ['show date', 'show myself', 'show status', 'show version active', 'show version inactive',
                 'show dscp all', 'utils service list', 'utils dbreplication status',
                 'utils dbreplication runtimestate', 'utils network arp list']

#cos_commands = ['show open ports all']

for command in ucos_commands:
    print('=============== ' + command + ' ===============' + '\n')
    output = net_connect.send_command(command + '\n', delay_factor=7)
    print(output + '\n')
    #fileout.write(output)

net_connect.disconnect()
sys.stdout = cleanslate
fileout.close()
#raise SystemExit


print('Pelaksanaan Perintah Selesai')
print('\n')
try:
    input("Press Enter to Continue..")
except SyntaxError:
    pass