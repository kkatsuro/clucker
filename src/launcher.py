#!/usr/bin/python3

import socket
import sys
import subprocess

# Wrapper for gui.py, @todo: move this code to gui.py.

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('', 12748))
        data = s.recv(6)
        if data == b'done!':
            print('connected! window should appear..')
            sys.exit(0)

except Exception as e:
    print('error:', e)

print('starting process')
GUI_PATH = './gui.py'
subprocess.Popen([GUI_PATH])
