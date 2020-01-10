A = [2, 4, 7, 5, 22, 11]
def findSum(arr):
    total = 0
    for i in arr:
        total += i
    return total

def findMult(arr):
    total = 1
    for i in arr:
        total *= i
    return total

def findCond(setA):
    n = len(setA)
    maxi = setA[0]
    mini = setA[0]
    for i in range(1, len(setA)):
        if setA[i] > maxi:
            maxi = setA[i]
        if setA[i] < mini:
            mini = setA[i]
    return (maxi+mini)*(n/4)

def subsets(setA):
    optimal = setA.copy()
    condition = findCond(setA)
    return generate_subB([], setA, 0, condition, optimal)

def generate_subB(temp, setA, start,condition, optimal):
    if(findSum(temp) >= condition and findMult(temp) < findMult(optimal)):
        optimal = temp.copy()
    for i in range(start, len(setA)):
        temp.append(setA[i])
        optimal = generate_subB(temp, setA, i + 1, condition, optimal)
        temp.pop()
    return optimal
        

print(subsets(A))