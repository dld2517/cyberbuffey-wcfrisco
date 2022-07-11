import socket
s = socket.socket()
s.settimeout(2)

target = 'target1.bowneconsulting.com'

s.connect((target, 80))
req = 'HEAD / HTTP/1.1\r\nHost: ' + target + '\r\n\r\n'
s.send(req.encode())
print(s.recv(1024).decode())
s.close()

