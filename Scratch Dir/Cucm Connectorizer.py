#from xcelip import iprecs
from netmiko.linux import LinuxSSH
from netmiko import ConnectHandler
import os
import errno
import datetime
import time
from IPy import IP
from colorama import init
import sys

timestamp = time.strftime(".%H%M%S")

print('\033[31m' + 'This is a Python scrip to generate pre-defined commands for Cisco IOS and IOS XE devices,')
print('Files will be pulled from excel rows and saved in each individual text files according to IP Address')
print('Normal device config generation time and resources consumption still applies.')
print('v0.1 Alpha')
init(wrap=False)
cleanslate = sys.stdout
try:
    ipaddr = input('Please enter IP Address : ') # Manual IP Prompt
    #ipaddr = iprecs # Pull data through excel file from xcelip module
    IP(ipaddr)
except ValueError:
    print('Invalid Ip Detected')
    sys.exit(1)

username = input('Please enter username : ')
password = input('Please enter device password : ')
cisco_devices = {
    'device_type': 'linux',
    'ip': ipaddr,
    'username': username,
    'password': password,
    'global_delay_factor': 20,
}

#if not os.path.exists("C:/sshoutput/"): # Test block for cuscomized target direcotory
    #os.mkdir("C:/sshoutput/")
#path = 'C:/sshoutput/'

"""filename = ipaddr + str(timestamp) + '.txt'"""
print('Generating.....' )
net_connect = ConnectHandler(**cisco_devices)

fileout = open(ipaddr + str(timestamp) + ".txt", "a")i
sys.stdout = fileout
ucos_commands = ['show date', 'show myself', 'show status', 'show version active', 'show version inactive']

for command in ucos_commands:
    print('=============== ' + command + ' ===============' + '\n')
    output = net_connect.send_command(command + '\n', delay_factor=2)
    print(output + '\n')
    #file.write(output)

net_connect.disconnect()
sys.stdout = cleanslate
fileout.close()
#raise SystemExit

try:
    input("Press enter to continue")
except SyntaxError:
    pass