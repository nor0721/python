import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect("192.168.43.162", username="pi", password="raspberry")
#ssh.connect("192.168.43.162", username="pi", password="raspberry")

stdin, stdout, stder = ssh.exec_command("ls")
print str(stdout.read())
stdin, stdout, stder = ssh.exec_command("cd Documents/ && ls && sudo pyhton serial_test1.py && a")
print str(stdout.read())
stdin, stdout, stder = ssh.exec_command("ls")
print str(stdout.read())
#stdin, stdout, stder = ssh.exec_command("sudo python serial_test1.py")
#print str(stdout.read())
#stdin, stdout, stder = ssh.exec_command("a")
#print str(stdout.read())
#stdin, stdout, stder = ssh.exec_command("b")
#print str(stdout.read())
#stdin, stdout, stder = ssh.exec_command("x")
#print str(stdout.read())
#stdin, stdout, stder = ssh.exec_command("sudo uname -a")
#print str(stdout.read())
#ssh.exec_command("sudo shutdown")

ssh.close()
