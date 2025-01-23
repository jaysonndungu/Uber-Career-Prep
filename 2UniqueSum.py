#Time complexity: O(n)
#Space complexity: O(n)


myList=[1,10,8,3,2,5,7,2,-2,-1]
'''
def uniqueSum(myList):
    uniqueList=[]
    sum=0
    for i in myList:
        if i not in uniqueList:
            uniqueList.append(i)
            sum+=i
    return sum

print(uniqueSum(myList))
#Time Taken: 4 minutes
'''

def uniqueSum(myList):
    uniqueDict={}
    sum=0 #initializing sum to 0
    for i in myList:
        if i not in uniqueDict: #if the number has not been seen
            uniqueDict[i]=1 #Adds a count to verify the number has been seen
            sum+=i #adds the unique number to the initialized sum
    return sum

print(uniqueSum(myList))





