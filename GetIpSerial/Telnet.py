__author__ = 'gong'
import getpass
import telnetlib

HOST = "192.168.2.22"
user = 'root'
password = 'Festo'
file = '/ffx/rcS'

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

command="ls %s\n"%(file)
tn.write(command.encode('ascii')) # convert string to bytes

#print(file.encode())


tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
