import socket
import re
s = socket.socket()
s.connect(("ad.samsclass.info", 10204))
for attempt in "abcde":
  sum=0
  r=(s.recv(1024).decode())
  print("Server response: ",r)
  num=re.findall(r'\d+',r)
  print(num)
  print(num[0]," ",num[1])
  if (r[0]=="A"):
    sum = str(int(num[0])+int(num[1]))
    print(sum)
  else:
    sum=str(int(num[0])-int(num[1]))
    print(sum)
  s.send(sum.encode())
  print(s.recv(1024).decode())
s.close()
