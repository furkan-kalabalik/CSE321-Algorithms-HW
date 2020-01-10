
prices = [0,1,5,8,9,10,17,17,20]
def rodCutProblem(prices,n):
    F =[]
    F.append(0)
    for i in range(1,n+1):
        j = 1
        temp = 0
        while(j <= i):
            temp = max(prices[j]+F[i-j], temp)
            j = j+1
        F.append(temp)
    return F[n]

print(rodCutProblem(prices,8))
    