from getpass import getpass
import paramiko
import sys


# Simple function to run a command and return decoded output
def run_command(command):
    stdin, stdout, stderr = client.exec_command(command)
    return stdout.read().decode()


if len(sys.argv) == 1:
    print("Usage: paramiko-demo.py <hostname|ip>")
    exit(1)

# Grab the hostname/ip from the passed arguments, ignore additional arguments
hostname = sys.argv[1]


# Define the management networks we expect to see routes for
management_networks = ["192.168.10.0/24", "172.17.0.0/16", "212.124.244.0/24"]


# Gather credentials
user_name = input("Username: ")
password = getpass()


# Initialise client, set host key policy and connect to server
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=user_name, password=password)


# Gather route details from remote server
output = run_command("/usr/sbin/ip route")
# routes = [line.split()[0] for line in output.strip().split("\n")]
routes = []
for line in output.strip().split("\n"):
    routes.append(line.split()[0])


# Cycle through management routes and check if it is present on the server
for network in management_networks:
    if network not in routes:
        print(f"Route for {network} is missing")
