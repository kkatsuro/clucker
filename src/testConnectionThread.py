import unittest
import logging
import sys

import time
import json

from ConnectionThread import ConnectionThread

with open('conf.json', 'r') as f:
    SERVER = list(json.loads(f.read())['servers'])[0]

class MockConsoleTab:
    def log(self, message):
        print(message)

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


if __name__ == '__main__':
    unittest.main()
