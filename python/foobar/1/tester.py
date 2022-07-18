
import re

string = 'abcabcabcdefabcabcabcdef'
match = list(re.finditer('a',string))
for a in match:
   print("a type: ",type(a))
   print("iter type: ",type(match))

        




