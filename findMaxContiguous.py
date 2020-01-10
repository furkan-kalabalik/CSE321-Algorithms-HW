A = [5, -6, 6, 7, -6, 7, -4, 3]
def maxCrossingSub(arr, low, mid, high):
    leftSum = float('-inf')
    total = 0
    maxLeft = 0
    maxRight = 0
    for i in range(mid, low, -1):
        total = total + arr[i]
        if (total > leftSum):
            leftSum = total
            maxLeft = i
    rightSum = float('-inf')
    total = 0
    for j in range (mid+1, high, 1):
        total = total + arr[j]
        if (total > rightSum):
            rightSum = total
            maxRight = j
    return maxLeft,maxRight,leftSum+rightSum

def findMaxSub(arr,low,high):
    if (high==low):
        return (low,high,arr[low])
    else:
        mid = (low+high)//2
        leftLow,leftHigh,leftSum = findMaxSub(arr,low,mid)
        rightLow,rightHigh,rightSum = findMaxSub(arr,mid+1,high)
        crossLow,crossHigh,crossSum = maxCrossingSub(arr, low, mid,high)
        if(leftSum >= rightSum and leftSum >= crossSum):
            return (leftLow,leftHigh,leftSum)
        if(rightSum >= leftSum and rightSum >= crossSum):
            return (rightLow,rightHigh,rightSum)
        else:
            return (crossLow,crossHigh,crossSum)



def printMaxSum(arr):
    low,high,maxSum = findMaxSub(arr, 0, len(arr)-1)
    print("Max sum is : %d"%(maxSum))
    print("Array part is", end=": ")
    for i in range(low,high+1):
        print (arr[i], end = " ")
    print()

printMaxSum(A)


