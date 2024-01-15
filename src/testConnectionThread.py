
import sys
sys.path.insert(0, '/home/meta/projects/python-modules')
# sys.path.insert(1, '/home/meta/src/paramiko/paramiko')
import threading

# import web_pdb; web_pdb.set_trace()

import unittest

import time
import json

from ConnectionThread import ConnectionThread

import threading

import faulthandler
faulthandler.enable()

import tracemalloc
tracemalloc.start()

from segfault import segfault

# @todo: we should do a mock server later?
# or is that too much effort to do all of these tests?
with open('conf.json', 'r') as f:
    SERVER = list(json.loads(f.read())['servers'])[0]

class MockConsoleTab:
    def log(self, message):
        print(message)

# so why it can't finish testing??...

class TestConnectionThreadMethods(unittest.TestCase):
    def test_connect_and_cancel(self):
        # @todo: create ssh server and connect to it on localhost?  or ask user to provide some
        print('creating connection thread')
        connection = ConnectionThread(SERVER, MockConsoleTab())
        while not connection.initialized:
            time.sleep(0.01)

        connection.cancel()

        while connection.is_alive():
            time.sleep(0.01)


        print(connection, flush=True)
        self.assertFalse(connection.is_alive())

        # signal.raise_signal(signal.SIGSEGV)

def test_myself():
    # @todo: create ssh server and connect to it on localhost?  or ask user to provide some
    print('creating connection thread')
    connection = ConnectionThread(SERVER, MockConsoleTab())
    while not connection.initialized:
        time.sleep(0.01)

    connection.cancel()

    while connection.is_alive():
        time.sleep(0.01)

    print(connection, flush=True)

if __name__ == '__main__':
    test_myself()
    print('active threads left:', threading.active_threads_count)
    # segfault()
    # unittest.main()
    
