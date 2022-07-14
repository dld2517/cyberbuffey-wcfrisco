
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
