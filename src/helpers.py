#!/usr/bin/python3.9

import random
import socket
import os
import subprocess
import os
import sys
import time

from dataclasses import dataclass, field

def extract_cogname_from_path(path):
    if path[-1] == '/':
        path = path[:-1]
    return path.split('/')[-1]

def port_is_available(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = False
    try:
        sock.bind(("0.0.0.0", port))
        result = True
    except:
        print("Port already in use")
    sock.close()
    return result

def get_random_available_port():
    num = random.randint(1024, 49151)
    while not port_is_available(num):
        num = random.randint(1024, 49151)
    return num

def combobox_clear(combobox):
    while combobox.count():
        combobox.removeItem(0)

def widgetlist_clear(combobox):
    while combobox.count():
        combobox.takeItem(0)

# @todo: Currently this function is not certain, we probably should add some way of better identification.
# For example, __init__.py common for a python package, but __init__ with:
# `def setup(bot):
#     bot.add_cogs(our_cog)`
# is not.
def is_cog_path(path):
    '''Checks if directory is (probably) a cog directory.'''
    return '__init__.py' in os.listdir(path)  # info.json is not needed for cog to be loaded, but it is standard file too.


# == previously find_pythons.py ==

def probably_is_python(path):
    # It will take too much time and resources to run subprocess on every executable on system, or execute IPython. So we do different things to exclude some executables as not Python ones.

    if 'python' not in path:  
        return False

    try:
        with open(path, 'r') as f:  # Hopefully unicodeDecodeError will happen on every binary.
            f.read(20)
        return False

    except OSError:  # OSError happens on Windows with dumb python.exe which opens Microsoft Store for installation.
        return False

    except UnicodeDecodeError: 
        pass

    return True
    
# This isn't 100% certain, so when used, give user an option to specify path of Python if it couldn't find it.
def find_all_python_binaries():
    probably_pythons = set()
    for directory in os.get_exec_path():
        try:
            files = { f'{directory}/{name}' for name in os.listdir(directory) }
        except:
            continue

        probably_pythons |= { file for file in files if probably_is_python(file) }

    # @todo: This may cause lag on older machines...
    processes = [
        subprocess.Popen( [ path, '-c', 'print("THIS IS PY SCRIPT", end="")' ],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL
        ) for path in probably_pythons
    ]

    python_versions = set()
    for process in processes:
        try:
            process.wait(timeout=0.2)
        except subprocess.TimeoutExpired:
            continue
        if process.returncode == 0 and process.stdout.read() == b'THIS IS PY SCRIPT':
            python_versions.add(process.args[0])


    return list({ os.path.realpath(path) for path in python_versions })

# @todo: This may be unnecessary.
@dataclass
class PythonVersion:
    path: str
    version: str = field(init=False)

    def __post_init__(self):
        self.version = subprocess.run(
            [self.path, '--version'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL
        ).stdout.decode().split()[1]

    def __str__(self):
        return f'Python {self.version} - {self.path}'

# Some simple tests, @todo: Implement this correctly.
def main():
    start = time.time()
    pythons = [ PythonVersion(path) for path in find_all_python_binaries() ]
    print(pythons)
    print('executed in time:', round(time.time() - start, 2), 'seconds')
    # @Todo: It takes 0.44 seconds on my computer now, maybe we want to optimize even more.

if __name__ == "__main__":
    main()
