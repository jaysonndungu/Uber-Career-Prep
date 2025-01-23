#Time Complexity = O(n)
#Space Complexity= O(n)

'''
def FirstOccurence(myString):
    uniqueList=[]
    stringOutput=""
    for i in myString:
        if i not in uniqueList:
            uniqueList.append(i)
            stringOutput+=i
    return stringOutput

print(FirstOccurence("Uber Career Prep"))
'''
#Time Taken= 5 minutes

def FirstOccurence(myString):
    myDict={}
    #Using a list(to hold the return value) instead of a string for better memory allocation. Since a string is immutable, concantenation creates a copy and therefore more allocated space.
    stringOutput=[]
 
    for i in myString:  #iterate directly over the characters
        if i not in myDict: #O(1) lookup
            stringOutput.append(i)
            myDict[i]=1 #sets a key,value pair

#Making the list into a string for better memory allocation
    return "".join(stringOutput)

print(FirstOccurence("Uber Career Prep"))



