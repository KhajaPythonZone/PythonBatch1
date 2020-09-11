#!/usr/bin/env python3

from paramiko import SSHClient, AutoAddPolicy


def check_ssh_connection(ipaddress, username, password):
    """
    This function will accept host details
    :param ipaddress: ipaddress of the host
    :param username: username of the host
    :param password: password of the host
    :return: True if connected false otherwise
    """
    ssh_client = SSHClient()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())
    ssh_client.load_system_host_keys()
    ssh_client.connect(hostname=ipaddress, username=username, password=password)
    ssh_client.close()
    return True


if __name__ == "__main__":
    if check_ssh_connection(ipaddress='54.212.181.50', username='testuser', password='testuser'):
        print("success")
    else:
        print("failed to connect")
