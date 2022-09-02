# Figure out which display output we're using and write it to a specified file

import subprocess
import sys

xrandr_output = subprocess.check_output('xrandr')

for line in xrandr_output.splitlines():
    line = line.decode("utf-8")
    line = line.split(' ')
    if line[1] == 'connected':
        print(f'ansible-digital-signage: Detected the display output as {line[0]}')
        with open(sys.argv[1], 'w') as outfile:
            outfile.write(line[0])
        exit(0)
