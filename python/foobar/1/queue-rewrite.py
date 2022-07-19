import re
# string = 'abcdeabcdeabcdeabcdeabcdeabcde'
string = 'abccbaabccba'
# string = 'abcdabababcdabababcdabab'
# string = 'abcabababcabcabababcabcabababcabcabababc'
firstChar = string[0]
groupCounts = []
indexList = []
splitList = re.finditer(firstChar,string)
for j in splitList:
  tempChar=j
  indexList.append(j.span()[0])
elements=len(indexList)
lastIndex=0
del indexList[0]
for a in indexList:
    finalIndex=a
    subString = string[lastIndex:finalIndex]
    lastIndex = a
    groupCounts.append(len(subString))
groupCounts.append(len(string[lastIndex:]))
modVals=[]
for c in range(2,len(groupCounts)):
    modResult = len(groupCounts) % c
    if modResult == 0:
        modVals.append(c)
compareList = []
smashSet = []
for b in modVals:
    if len(set(groupCounts)) == 1:
        print("There are ",elements, " slices of cake.")
        break
    compareList=[]
    iterI = 0
    while True:
        compareList.append(groupCounts[iterI:iterI+b])
        iterI += b
        if iterI >= len(groupCounts):
            for lst in compareList:
                smashSet.append(tuple(lst))
            finalSet = set(tuple(smashSet))
            break
        try:
            finalSet
        except NameError:
            varExists = False
        else:
            varExists = True 
        if varExists:
            if len(finalSet) == 1:
                print("Answer is: ",b," slices of cake")
                break


