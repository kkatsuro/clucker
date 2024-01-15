#!/usr/bin/python3.9

import subprocess
import shutil
import time
import websocket

from helpers import *

import json
import os

CO_OWNERS = [ '992441146754224128' ]

# @todo: Does this make sense? We access this directory in few places, and this thanks to this code we can be certain it exists. But someone can remove it during program execution, so better idea is probably to do it every time it is accessed? But then, if redbot runs inside this directory and it will be removed, whole program would break anyway, so I'm not sure if there's any point to look at things like that.
VENV_DIR = '/home/meta/.local/share/clucker/'  # @todo: Change this to $HOME
try:
    os.makedir(VENV_DIR)  
except:
    pass


def wizard_mock():
    py = PythonVersion('/usr/bin/python3.9')
    redbot = '3.4.18'

    # venv_path = install_redbot_venv(py.path, redbot)
    # setup_instance('kurisu', venv_path, redbot)

    instance = red_instance
    red = start_red_process(instance, open(f'/dev/pts/3', 'w'))

    try:
        reload_cog(instance, '/home/meta/projects/kurumi/fap/fap')
    except Exception as e:
        print('exception!!')
        print(str(e))

    red.terminate()
    
if __name__ == "__main__":
    wizard_mock()
