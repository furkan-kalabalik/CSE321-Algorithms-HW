NY = [None, 1,3,20,30]
SF = [None, 50,20,2,4]

def BusinessPlan(ny,sf,n,M):
    F = []
    for i in range(len(ny)):
        F.append(0)
    F[1] = min(ny[1],sf[1])
    if(F[1] == ny[1]):
        lastCity = 0
    else:
        lastCity = 1
    for j in range(2,len(ny)):
        if(lastCity == 0):
            op1 = ny[j]
            op2 = sf[j]+M
        else:
            op1 = ny[j]+M
            op2 = sf[j]
        F[j] = F[j-1] + min(op1,op2) 
        if(min(op1,op2) == op1):
            lastCity = 0
        else:
            lastCity = 1
    return F[n]

print(BusinessPlan(NY,SF,4,10))