import paramiko

router_ip = "10.1.1.5"
router_username = "admin"
router_password = "Cisco123"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(router_ip, username=router_username, password=router_password,allow_agent=False, look_for_keys=False)

# Run command.
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("show ip route")

output = ssh_stdout.readlines()
# Close connection.
ssh.close()

# Analyze show ip route output
for line in output:
    if "0.0.0.0/0" in line:
        print("Found default route:")
        print(line)




# Option 2

import paramiko as paramiko
from paramiko import AutoAddPolicy

router_ip = "10.1.1.5"
router_username = "admin"
router_password = "Cisco123"



ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect(router_ip, username=router_username, password=router_password,allow_agent=False, look_for_keys=False)

# Run command.
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("show app-hosting list")

output = ssh_stdout.readlines()
# Close connection.
ssh.close()

# Analyze show ip route output
for line in output:
    print(line)
 
 