arr = [[37, 23, 22, 32], [21,6,7,10], [53, 34, 30, 31], [32, 13, 9, 6], [43, 21, 15, 8]]
arr1 = [[37, 23, 22, 32]]

def print2d(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print ("%2d" %(arr[i][j]), end=" ")
        print()

def specialCheck(arr):
    count = 0
    for i in range(len(arr)-1):
        for j in range(len(arr[0])-1):
            if(arr[i][j]+arr[i+1][j+1] > arr[i][j+1]+arr[i+1][j]):
                count = count + 1
                left = arr[i][j]+arr[i+1][j+1]
                right = arr[i][j+1]+arr[i+1][j]
                dif = left - right
                arr[i][j+1] = arr[i][j+1]+dif
    if(count == 1):
        print2d(arr)
    else:
        print("It requires more than 1 change")

print("Before change")
print2d(arr)
print("After change")
specialCheck(arr)

def getLeftMostMin(arr):
    min = arr[0]
    minIndex = 0
    for i in range(1, len(arr)):
        if(arr[i] < min):
            min = arr[i]
            minIndex = i
    return minIndex

def findMins(arr,start,end,index):
    if (start == end):
        index.append(getLeftMostMin(arr[start]))
    else:
        if((end-start)%2==0):
            half = (end-start)//2
            findMins(arr, start, half-1, index)
            findMins(arr, half, half,index)
            findMins(arr, half+1, end, index)
        else:
            half = ((end-start)//2)+start
            findMins(arr, start, half, index)
            findMins(arr, half+1, end, index)

def minRow(arr):
    index = []
    findMins(arr, 0, len(arr)-1, index)
    return index

print (minRow(arr))

    

