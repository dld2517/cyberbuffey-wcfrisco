key = "Unbreakable awesome secret secure system"
ciphertext = bytes.fromhex("130117004512080e100945410f1345000a1b004e")
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
