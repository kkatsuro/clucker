import threading

class ThreadREEE(threading.Thread):
    def __init__(self, name=None):
        super().__init__(name=name)

    def run(self):
        print(f'{self.name} running..')
        print('and from current_thread() now:', threading.current_thread().name)

print('current_thread():', threading.current_thread().name)

a = ThreadREEE()
a.start()
a.join()

print('reeeeeeeeee')
