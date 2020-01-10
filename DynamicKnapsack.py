weight = [None,2,1,3,2]
value = [None,12,10,20,15]
total = 5

knapsack = []
for i in range(len(value)):
    inside = []
    for j in range(total+1):
        inside.append(0)
    knapsack.append(inside)

def print2d(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()

for i in range(1,len(value)):
    for j in range(1,len(knapsack[0])):
        if (j >= weight[i]):
            knapsack[i][j] = max(knapsack[i-1][j],value[i]+knapsack[i-1][j-weight[i]])
        else:
            knapsack[i][j] = knapsack[i-1][j]

print2d(knapsack)