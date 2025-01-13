#Time complexity: O(n)
#Space complexity: O(n)


myList=[1,10,8,3,2,5,7,2,-2,-1]

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






