"""
Created on Aug 10, 2018

@author: Anshul
"""

#!/usr/bin/python
import os
from getpass import getpass

import paramiko


def deploy_key(key, server, username, password):
    """
    Function to copy keys to servers
    :param key:
    :param server:
    :param username:
    :param password:
    :return:
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, username=username, password=password)
    client.exec_command('mkdir -p ~/.ssh/')
    client.exec_command('echo "%s" > ~/.ssh/authorized_keys' % key)
    client.exec_command('chmod 644 ~/.ssh/authorized_keys')
    client.exec_command('chmod 700 ~/.ssh/')


if __name__ == '__main__':
    key = open(os.path.expanduser('~/.ssh/id_rsa.pub')).read()
    username = os.getlogin()
    password = getpass()
    hosts = ["hostname"+str(i) for i in range(1, 101)]
    for host in hosts:
        deploy_key(key, host, username, password)


#  ############################################################################################
#  I can use some multi htreading here. But I don't want to as a of now.
#  Python has threading module, and Thread class

#  We can also use some modules called 'ssh-copy-id' which I haven't get any real time experience as of now.
#  ######################################################################################################



