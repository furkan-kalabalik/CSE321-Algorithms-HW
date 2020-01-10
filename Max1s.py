def maxOnesSquare(arr):
    result=[]
    val = []
    for i in range(len(arr)+2):
        for j in range(len(arr)+2):
            val.append(0)
        result.append(val)
    for

def print2d(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=" ")
        print()

arr = [[0,1,1,0,1],[1,1,1,0,0],[1,1,1,1,0],[1,1,1,0,1]]
maxOnesSquare(arr)