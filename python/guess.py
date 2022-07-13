#This is the crib drag attack

key="The"
# a=bytes.fromhex(input("Cipher Text 1: "))
# b=bytes.fromhex(input("Cipher Text 2: "))
a=bytes.fromhex("13070b4954491b53114816450d1b101c100000090952480105044e4b000f4b4e5453")
b=bytes.fromhex("070d0a1e4c0c4e4d1d0f0d54431c10175311480a464604140a5b4e64373722233153")

i=0
while(True):
    print()
    print("     0123456789012345678901234567890123456789")
    print("Key:", key)
    print()
    print()
    plaintext = ""
    for p in a:
        k= key[i]
        ik = ord(k)
        ip = p^ik
        z=chr(ip)
        print(k,"\t",chr(a[p]),"\t",chr(b[p]))
        plaintext += str(p)
        i += 1
char = int(input("Which character? "))
val=input("value: ")
key=key[0:char] + val + key[char+1:]
print(plaintext)
