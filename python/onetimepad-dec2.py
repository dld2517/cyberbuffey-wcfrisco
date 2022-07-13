key = "Wow, what a great key!"
ciphertext = bytes.fromhex("0e20220c67383c413d7440")
i = 0
plaintext = ""
for c in ciphertext:
  k = key[i]
  ik = ord(k)
  ip = c ^ ik
  p = chr(ip)
  print(c, k, ik, ip, p)
  plaintext += p
  i += 1
print(plaintext)
