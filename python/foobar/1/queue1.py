import re
string = 'abccbaabccba'
# string = 'abcdeabcdeabcdeabcdeabcdeabcde'
# string = 'abcdabababcdabababcdabab'
# string = 'abcabababcabcabababcabcabababcabcabababc'
firstChar = string[0]
print("string is: ",string,"  first char is: ",firstChar)
groupCounts = []
indexList = []
smashSet = []
splitList = re.finditer(firstChar,string)
for j in splitList:
  print(j)
  tempChar=j
  indexList.append(j.span()[0])
elements=len(indexList)
print("There are ",elements, " in the list.")
print()
print()
lastIndex=0
del indexList[0]
for a in indexList:
    print("a: ",a," lastIndex: ",lastIndex)
    finalIndex=a
    print(lastIndex,finalIndex)
    subString = string[lastIndex:finalIndex]
    lastIndex = a
    print(subString)
    groupCounts.append(len(subString))
groupCounts.append(len(string[lastIndex:]))
print("Here is the ordered list of character counts")
for num in groupCounts:
    print(num)
    print("num: ",type(num))
    print("groupcounts: ",type(groupCounts))
print("Number of records in the list")
print("Number: elements: ",elements)
print("Length Groupcounts",len(groupCounts))

# Let's check to see if groupCounts are all the same before we launch off itnto mods


"""
for lst in groupCounts:
    print("lst: ",type(lst))
    print("groupCount: ",type(groupCounts))
    try:
        smashSet
    except:
        NameError
        smashSet=set([])
    else:
        smashSet.append(tuple(lst))
    
checkSet=set(tuple(smashSet))
"""

print('List of MOD values')

modVals=[]
for c in range(2,len(groupCounts)):
    print(c)
    modResult = len(groupCounts) % c
    if modResult == 0:
        modVals.append(c)
    print(len(groupCounts), " MOD ", c, " is ", modResult)
  
print("List of Modulo values to try")
for d in modVals:
    print(d)

# setup for the parsing
""" what I am trying to do here is work through list (groupCounts) and take the first modVals[i] entries and pop to compareList
    then I can compare the first entry of every list to see if it is the same, if it is, then campare the second, etc
    each time allowing a break to decide that it is different
"""
compareList = []
for b in modVals:
    if len(set(groupCounts)) == 1:
        print("There are ",elements, " slices of cake.")
        break
    print("B is: ",b)
    compareList=[]
    iterI = 0
    print(groupCounts)
    while True:
        compareList.append(groupCounts[iterI:iterI+b])
        print("IterI: ",iterI, " B: ",b, "Len GroupCnt: ", len(groupCounts), "GroupCount: ",groupCounts[iterI:iterI+b])
        iterI += b
        print(compareList)
        print("IterI: ",iterI)
        if iterI >= len(groupCounts):
            print("Hit the if condition len groupcounts")
            for lst in compareList:
                smashSet.append(tuple(lst))
                print(smashSet)
            print("done with comparelist loop")
            finalSet = set(tuple(smashSet))
            print("finalset is below")
            print(finalSet)
            break
        try:
            finalSet
        except NameError:
            varExists = False
            print("on nameerror")
        else:
            varExists = True 
        if varExists:
            if len(finalSet) == 1:
                print("Answer is: ",b," slices of cake")
                break

print(groupCounts)
print(compareList)
print(modVals)






