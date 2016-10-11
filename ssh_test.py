import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect("192.168.43.162", username="pi", password="raspberry")

#stdin, stdout, stder = ssh.exec_command("sudo uname -a")
#print str(stdout.read())
ssh.exec_command("sudo shutdown")

ssh.close()
