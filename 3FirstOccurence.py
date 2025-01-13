#Time Complexity = O(n)
#Space Complexity= O(n)


def FirstOccurence(myString):
    uniqueList=[]
    stringOutput=""
    for i in myString:
        if i not in uniqueList:
            uniqueList.append(i)
            stringOutput+=i
    return stringOutput

print(FirstOccurence("Uber Career Prep"))

#Time Taken= 5 minutes


