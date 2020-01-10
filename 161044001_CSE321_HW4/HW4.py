def specialArrayDriver():
    arr = [[37, 23, 22, 32], [21,6,7,10], [53, 34, 30, 31], [32, 13, 9, 6], [43, 21, 15, 8]]
    print("-----------SPECIAL ARRAY DRIVER-------")
    print()
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
    
    print()
    print()
    print("Indexes of minimum element of rows of special array:", end=" ")
    print (minRow(arr))
    print()
    print()

def findKthDriver():
    print("-----------FIND KTH DRIVER-------")
    print()
    print("Array1:", end=" ")
    arr1 = [1,2,3]
    print(*arr1, end=" ")
    print()
    arr2 = [4,5,6]
    print("Array2:", end=" ")
    print(*arr2, end=" ")
    print()
    k = 3
    def findKth(arr1, start1, end1, arr2, start2, end2, k):
        if end1 - start1 < 0:
            return arr2[start2 + k]
        if end2 - start2 < 0:
            return arr1[start1 + k]
        if k == 0:
            return min(arr1[k + start1], arr2[k + start2])
        arr1MidIndex = (start1 + end1) // 2
        arr2MidIndex = (start2 + end2) // 2
        arr1Mid = arr1[arr1MidIndex]
        arr2Mid = arr2[arr2MidIndex]
        
        if ((arr1MidIndex - start1) + (arr2MidIndex - start2) < k):
            if(arr1Mid > arr2Mid):
                return findKth(arr1, start1, end1, arr2, arr2MidIndex+1, end2, k - (arr2MidIndex-start2) -1)
            else:
                return findKth(arr1, arr1MidIndex+1, end1, arr2, start2, end2, k - (arr1MidIndex-start1) - 1)
        else:
            if(arr1Mid > arr2Mid):
                return findKth(arr1, start1, arr1MidIndex-1, arr2, start2, end2, k)
            else:
                return findKth(arr1, start1, end2, arr2, start2, arr2MidIndex-1, k)
    print("%d th element is: %d"%(k, findKth(arr1,0,len(arr1)-1, arr2, 0, len(arr2)-1,k)))
    print()
    print()

def maxContiguousSubDriver():
    print("-----------MAX CONTIGUOUS SUBARRAY DRIVER-------")
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

    low,high,maxSum = findMaxSub(A, 0, len(A)-1)
    print("Array is:", end=" ")
    print(*A, end=" ")
    print()
    print("Max sum is : %d"%(maxSum))
    print("Array part is", end=": ")
    for i in range(low,high+1):
        print (A[i], end = " ")
    print()
    print()

def bipartiteGraphCheckDriver():
    print("-----------BIPARTITE CHECKER DRIVER-------")
    graph = {0: [1,2], 1:[0,3],2:[0,3],3:[1,2]}
    print()
    for i in range(len(graph)):
        print("Node %d Adjacency List:"%(i), end = " ")
        for j in range(len(graph[i])):
            print(graph[i][j], end=" ")
        print()

    def check_bipartite_dfs(graph):
        visited = []
        color = []
        for i in range(len(graph)):
            visited.append(False)
        
        for i in range(len(graph)):
            color.append(2)
        
        for i in range(len(graph)):#Maybe this is directional graph
            if not visited[i]:
                dfs(i, 0,visited,color)
    
        for i in range(len(graph)):
            for j in graph[i]:
                if color[i] == color[j]:
                    return False
        return True

    def dfs(vertex, colored,visited,color):
        visited[vertex] = True
        color[vertex] = colored
        for u in graph[vertex]:
            if not visited[u]:
                dfs(u, 1 - colored,visited,color)
    print("Is graph biparite? -",end=" ")
    print(check_bipartite_dfs(graph))
    print()
    print()

def bestDayToBuyAndSellDriver():
    print("-----------BEST DAY to BUY and SELL DRIVER-------")
    print()
    print("Costs:", end=" ")
    C = [5,11,2,21,5,7,8,12,13,None]
    print(*C, end=" ")
    print()
    print("Prices:", end=" ")
    P=[None,7,9,5,21,7,13,10,14,20]
    print(*P, end=" ")
    print()
    print()
    def isProfit(startDay, gain):
        if(gain > 0):
            return True, startDay, gain
        else:
            return False, startDay,gain

    def findMaxProfitDay(cost,start,end,price):
        if(end - start == 1):
            return isProfit(start, price[end]-cost[start])
        else:
            if((end-start)%2 == 0):
                mid = ((end-start)//2)+start
                isGainLeft, leftStart,leftGain = findMaxProfitDay(cost,start,mid,price)
                isGainRight, rightStart,rightGain = findMaxProfitDay(cost,mid,end,price)
                if(leftGain > rightGain):
                    return isProfit(leftStart, leftGain)
                else:
                    return isProfit(rightStart, rightGain)
            else:
                mid = ((end-start)//2)+start
                isGainLeft, leftStart,leftGain = findMaxProfitDay(cost,start,mid,price)
                isGainMid, midStart,midGain = findMaxProfitDay(cost,mid,mid+1,price)
                isGainRight, rightStart,rightGain = findMaxProfitDay(cost,mid+1,end,price)
                if(leftGain>midGain and leftGain >rightGain):
                    return isProfit(leftStart,leftGain)
                elif(rightGain>midGain and rightGain>leftGain):
                    return isProfit(rightStart, rightGain)
                else:
                    return isProfit(midStart,midGain)

    def printBestSellDay(cost,price):
        isGain, day, gainUnit = findMaxProfitDay(cost,0,len(cost)-1,price)
        if(isGain):
            print("Best days to buy and sell:%d-%d and gain for 500 unit will be:%d"%(day+1, day+2,gainUnit*500))
        else:
            print("No day to make money")

    printBestSellDay(C,P) 
    print()
    print()

def driver():
    specialArrayDriver()
    findKthDriver()
    maxContiguousSubDriver()
    bipartiteGraphCheckDriver()
    bestDayToBuyAndSellDriver()

driver()