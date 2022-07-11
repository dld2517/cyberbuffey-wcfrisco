import socket
s = socket.socket()
s.connect(("ad.samsclass.info", 10204))
r=(s.recv(1024).decode())
print(r)
num=""
if (r[1]=="A"):
  for c in r:
    if c.isdigit():
      num=num+c
  print(num)
else:
  for c in r:
    if c.isdigit():
      num=num+c

print("num is: ",num)

# s.send("43\n".encode())
print(s.recv(1024).decode())
s.close()
