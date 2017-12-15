#from xcelip import iprecs
from netmiko import ConnectHandler
import os
import errno
import datetime
import time
from IPy import IP
from colorama import init, Fore, Back, Style
import sys
import getpass

timestamp = time.strftime(".%H%M%S")

__author__ = "John Ng"
__copyright__ = "Copyright 2018, John Ng"
__license__ = "MIT License"
__version__ = "v1.0 Beta"
__status__ = "Experimental"

init(strip=False)
print('\033[31m' + 'This is a Python script to generate pre-defined commands for Cisco IOS, IOS XE, CatOS devices,')
print('IPs will be pulled from excel file and saved in each individual text files according to IP Address & timestamp')
print('Please Note...Normal device config generation time and resources consumption still applies.')
print(Fore.CYAN + Style.BRIGHT + '[v1.0 Beta]')
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
password = input('Please enter device password : ')
#password = getpass.getpass(prompt='Please enter device password : ')
secret = input('Please enter enable password : ')
#secret = getpass.getpass(prompt='Please enter enable password : ')
cisco_devices = {
    'device_type': 'cisco_ios',
    'ip': ipaddr,
    'username': username,
    'password': password,
    'secret': secret,
    'global_delay_factor': 2,
}
#if not os.path.exists("C:/sshoutput/"): # Test block for cuscomized target direcotory
    #os.mkdir("C:/sshoutput/")
#path = 'C:/sshoutput/'

fileout = open(ipaddr + str(timestamp) + ".txt", "a")
print('Generating.....')
sys.stdout = fileout
#net_connect2 = ConnectHandler(**cisco_devices)
net_connect = ConnectHandler(**cisco_devices)
ios_commands = ['show clock', 'show version', 'show inventory raw', 'show env all',
                'show ip int bri', 'show log', 'show process cpu sorted',
                'show process cpu history', 'show memory', 'show memory sorted', 'show cdp nei', 'show ip route',
                'show switch']
net_connect.enable()
net_connect.send_command('term len 0')

for command in ios_commands:
    print('=============== ' + command + ' ===============' + '\n')
    output = net_connect.send_command_expect(command)
    print(output + '\n')
outrun = net_connect.send_command('show run')
print('=============== ' + 'show run' + ' ===============' + '\n' + outrun)

net_connect.disconnect()
sys.stdout = cleanslate
fileout.close()

print('Pelaksanaan Perintah Selesai')
print('\n')
try:
    input("Press Enter to Continue..")
except SyntaxError:
    pass


"""
output = net_connect.send_command('show ip int brief')
print(output, file=open(ipaddr + str(timestamp) + ".txt", "a"))
print(output)
sys.stdout = orig_outp
f.close()
"""