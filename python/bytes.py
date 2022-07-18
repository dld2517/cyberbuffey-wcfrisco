a=b'\xFF'
print(a,type(a))
b=a[0]+1
print(b,type(b))


a=bytes.fromhex("13070b4954491b53114816450d1b101c100000090952480105044e4b000f4b4e5453")
b=bytes.fromhex("070d0a1e4c0c4e4d1d0f0d54431c10175311480a464604140a5b4e64373722233153")
total_length=len(a)

for num in range(total_length):
  print(a[num],"\t",b[num])


