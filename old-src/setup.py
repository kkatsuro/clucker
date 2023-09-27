from setuptools import setup, find_packages

setup(
    name='dozeoff-red-reloader',
    version='0.1.0',
    scripts=['rfap'],
    python_requires='>=3.8',
    install_requires=['docopt-ng', 'sshtunnel', 'jsonrpc_websocket' ],
)
