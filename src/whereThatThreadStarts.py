import threading
import paramiko
import sys

client = paramiko.client.SSHClient()
client.load_system_host_keys()
username, host = 'opc@some_ip'.split('@')
try:
    client.connect(host, username=username)

# @todo: what if error happens and we return below? - make the rest of app behave correctly
except paramiko.ssh_exception.AuthenticationException:
    print('authentication error!! try to change method from default')
    sys.exit()
except Exception as e:
    print('unknown error:')
    print(str(e))
    sys.exit()

print('connected!')

stdin, stdout, stderr = client.exec_command('echo "$HOME"')
home = stdout.read(4096).decode().strip()

print(f'home directory is {home}')

# start SFTP connection
sftp = client.open_sftp()
print(f'sftp opened')
transport = client.get_transport()

# @todo: start it according to current bot.. and maybe abstract into a bot class?
# forward_threads = []
# forward_threads.append(ForwardThread(6134, 'localhost', 6134, client.get_transport()))
print('started forward thread')

initialized = True
