import re
string = 'abcdefgabcdefgabcabcabcabcdefgabcdefgabcabcabc'
firstchar = string[0]
print("string is: ",string,"  first char is: ",firstchar)
indexlist=[]
splitlist = re.finditer(firstchar,string)
for j in splitlist:
  print(j)
  tempchar=j
  indexlist.append(j.span()[0])
elements=len(indexlist)
print("There are ",elements, " in the list.")
print()
print()
lastindex=0
del indexlist[0]
for a in indexlist:
    print("a: ",a," lastindex: ",lastindex)
    finalindex=a
    print(lastindex,finalindex)
    substring = string[lastindex:finalindex]
    lastindex = a
    print(substring)


print(string[0:3])
print(string[3:5])



"""
from collections import deque
myStack = deque()
print(len(myStack))
myStack.append('a')
myStack.append('b')
myStack.append('c')

print(len(myStack))
print(myStack)
myStack.pop()
print(len(myStack))
myStack.pop()
print(len(myStack))
"""
