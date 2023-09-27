#!/usr/bin/python3

import paramiko
import sys
import time

import os

# cog_path = '/


# some bot_find things
# sftp.chdir(home)
# print(sftp.getcwd())

# bots_dir = f'{home}/.local/share/Red-DiscordBot/data'

# try:
#     bots = sftp.listdir(bots_dir)
#     print(bots)
# except FileNotFoundError:
#     print('redbot dir not found')
#     sys.exit(1)

# .local/share/Red-DiscordBot/data/Kurisu/cogs/CogManager/cogs/

def update_directory(sftp, local_directory_path, remote_directory_path):
    # sftp = client.open_sftp()
    # stdin, stdout, stderr = client.exec_command('rm -rf ' + remote_directory_path)
    # stdout.read(4096)  # @todo: this one's necessary to make sure it was actually deleted. but is it reliable?

    if local_directory_path[-1] != '/':
        local_directory_path = local_directory_path + '/'

    if remote_directory_path[-1] != '/':
        remote_directory_path = remote_directory_path + '/'

    print('mkdiring... ', end='')
    sftp.mkdir(remote_directory_path)
    print('done')

    dir_stack = [ local_directory_path ]

    while len(dir_stack):
        current_dir = dir_stack.pop()

        print('dir scanning')
        for file in os.scandir(current_dir):
            # @todo: this replace is not very fast, but can this ever be a issue?
            new_path = file.path.replace(local_directory_path, remote_directory_path)  

            print(file.path, new_path, end='')

            if file.is_file():
                print(' - file put', end='')
                sftp.put(file.path, new_path)
            else:
                print(' - make directory', end='')
                sftp.mkdir(new_path)
                dir_stack.append(file.path)

            print(' - done!')

def do_everything(ip, hostname, local_path, remote_path):
    client = paramiko.client.SSHClient()
    client.load_system_host_keys()
    client.connect(ip, username=hostname)

    stdin, stdout, stderr = client.exec_command('echo "$HOME"')
    home = stdout.read(4096).decode().strip()

    update_dir(client, local_path, remote_path)

    # if sftp:
    #     sftp.close()

def main():
    # ip = ''
    # do_everything(ip, 'opc', '/home/meta/projects/clucker/secret-directory2/', '/home/opc/secret-directory-copy/')
    pass

if __name__ == '__main__':
    main()
