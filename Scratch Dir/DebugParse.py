from colorama import init
import re
import sys
# Test Parser to read debug files

print('This is a test script to read and define CUC Command output')
print('Script v0.1 Beta')

filename = input('Enter full file name with extension : ')
log_desc = []
pattern = re.compile("stopped",  re.IGNORECASE)
pattern2 = re.compile("DB Version", re.IGNORECASE)

try:
    with open(filename, 'rt') as log_name:
      for linenum, line in enumerate(log_name):
         if pattern.search(line) is not None:
            log_desc.append((linenum, line.rstrip('\n')))
            #for linenum, line in log_desc:
            print("- ", line, sep='')
except FileNotFoundError:
    print('Invalid File / File Not Found')
sys.exit(1)

