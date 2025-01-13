#Time Complexity: O(n)
#Space Complexity: O(n)

myList=[1,10,8,3,2,5,7,2,-2,-1]


def ZeroSum(myList):
    numPairs=0
    uniqueList=[]
    for i in range(len(myList)):
        if myList[i]*-1 in myList and abs(myList[i]) not in uniqueList:
            numPairs+=1
            uniqueList.append(abs(myList[i]))
    
    return numPairs


print(ZeroSum(myList))

#Could not figure out the Follow-Up in O(n)

#Time taken : 23 minutes
