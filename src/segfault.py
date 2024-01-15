import signal

def segfault():
    signal.raise_signal(signal.SIGSEGV)
