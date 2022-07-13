key = "Unbreakable awesome secret secure system"
plaintext = "Four score and seven"

i = 0
ciphertext = ""
for p in plaintext:
  ip = ord(p)
  k = key[i]
  ik = ord(k)
  inew = ip ^ ik
  ciphertext += chr(inew)
  print(p, hex(ip), k, hex(ik), hex(inew))
  i += 1
print(ciphertext.encode("ascii").hex())
