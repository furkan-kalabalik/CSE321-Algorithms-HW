def FirstQ():
    print("---------------------PART1---------------------")
    NY = [None, 1,3,20,30]
    SF = [None, 50,20,2,4]

    def BusinessPlan(ny,sf,n,M):
        F = []
        for i in range(len(ny)):
            F.append(0)
        F[1] = min(ny[1],sf[1])
        print("Sequence of business plan:",end=" ")
        if(F[1] == ny[1]):
            lastCity = 0
        else:
            lastCity = 1
        for j in range(2,len(ny)):
            if(lastCity == 0):
                print("NY", end=" ")
                op1 = ny[j]
                op2 = sf[j]+M
            else:
                op1 = ny[j]+M
                op2 = sf[j]
                print("SF", end=" ")
            F[j] = F[j-1] + min(op1,op2) 
            if(min(op1,op2) == op1):
                lastCity = 0
            else:
                lastCity = 1
        if(lastCity == 0):
            print("NY", end=" ")
        else:
            print("SF", end=" ")
        return F[n]
    cost = BusinessPlan(NY,SF,4,10)
    
    print()
    print("Total cost will be:", end=" ")
    print(cost)
    print("-----------------------------------------------")


def SecondQ():
    print("---------------------PART2---------------------")
    sessions = {2:[0,6], 4:[5,10], 1:[0,3], 3:[0,15],5:[8,12],6:[11,14],7:[15,17], 8:[16,22]}

    def SimulSession(sessions):
        sessions = {k: v for k, v in sorted(sessions.items(), key=lambda item: item[1])}
        print("Sessions sorted by finish time:", end=" ")
        for i in range(1,len(sessions)+1):
            print(i,end=" ")
        print()
        print("Sessions start time:", end="  ")
        for i in range(1,len(sessions)+1):
            print("%2d"%(sessions.get(i)[0]),end=" ")
        print()
        print("Sessions finish time:", end=" ")
        for i in range(1,len(sessions)+1):
            print("%2d"%(sessions.get(i)[1]),end=" ")
        print()
        lastTime = -1
        optimalSession = []
        for i in range(1,len(sessions)+1):
            if(sessions.get(i)[0] > lastTime):
                optimalSession.append(i)
                lastTime = sessions.get(i)[1]
        print("Optimal session with enter order:", end=" ")
        print(*optimalSession)

    SimulSession(sessions)
    print("-----------------------------------------------")


def ThirdQ():
    print("---------------------PART3---------------------")
    S = [-1, 6, 4, 2, 3, -7, -5]
    print("Given Array:", end=" ")
    print(S)
    S = sorted(S)
    neg = 0
    pos = 0
    target = 0
    for i in range(len(S)):
        if(S[i] > 0):
            pos += S[i]
        elif(S[i] < 0):
            neg += S[i]

    dp = [[True for i in range(pos-neg+1)] for j in range(len(S))]

    for i in range(len(S)):
        for j in range(neg, pos+1):
            if(i == 0):
                dp[i][j-neg] = (S[i] == j)
            elif(neg <= j - S[i] and j-S[i] <= pos):
                dp[i][j-neg] = (S[i] == j) or dp[i-1][j-neg] or dp[i-1][j-neg-S[i]]
            else:
                dp[i][j-neg] = (S[i] == j) or dp[i-1][j-neg]

    subset = []

    for i in range(len(S)-1, -1, -1):
        if(S[i] == target):
            subset.append(S[i])
        elif(not(dp[i-1][target-neg])):
            subset.append(S[i])
            target = target-S[i]

    isEqual = False

    for i in range(len(dp)):
        if(dp[i][-neg] == True):
            isEqual = True

    if(isEqual):
        print("Subset that sum is equal to zero:", end=" ")
        print(*subset)
    else:
        print("No subset like that")
    print("-----------------------------------------------")


def FourthQ():
    print("---------------------PART4---------------------")
    s1 = "ALGORITMA"
    s2 = "ALGORITHM"
    print("First sequence:", end=" ")
    print(s1)
    print("Second sequence:", end=" ")
    print(s2)

    DP_ROW_N = len(s1)+1 
    DP_COLUMN_N = len(s2)+1 
    match = 2
    mismatch = -2
    gap = -1

    dp = [[None for y in range(DP_COLUMN_N)] for x in range(DP_ROW_N)]

    for i in range(DP_ROW_N):
        dp[i][0] = mismatch*i
    for j in range(DP_COLUMN_N):
        dp[0][j] = mismatch*j

    for i in range(1,DP_ROW_N):
        for j in range(1,DP_COLUMN_N):
            score = (match if (s1[i-1] == s2[j-1]) else mismatch)
            m = dp[i-1][j-1] + score
            d = dp[i-1][j] + gap
            ins = dp[i][j-1] + gap
            dp[i][j] = max(m,d,ins)

    a1 = ""
    a2 = ""
    i = len(s1)
    j = len(s2)

    while (i > 0 or j > 0):
        if (i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + (match if (s1[i-1] == s2[j-1]) else mismatch)):
            a1 = s1[i-1] + a1
            a2 = s2[j-1] + a2
            i = i - 1
            j = j - 1
        elif (i > 0 and dp[i][j] == dp[i-1][j] + gap):
            a1 = s1[i-1] + a1
            a2 = "-" + a2
            i = i - 1
        else:
            a1 = "-" + a1
            a2 = s2[j-1] + a2
            j = j - 1
    print("Total cost will be:",end=" ")
    print(dp[len(s1)][len(s2)])
    print("First aligned sequence:",end=" ")
    print(a1)
    print("Second aligned sequence:",end=" ")
    print(a2)
    print("-----------------------------------------------")


def FifthQ():
    print("---------------------PART5---------------------")
    arr = [1, 3, 4, 2]
    print("Given array:", end=" ")
    print(arr)
    arr = sorted(arr)

    sum = 0
    operation = 0

    if(len(arr) < 2):
        print("No element to sum")
    else:
        sum = arr[0]+arr[1]
        operation += sum

        for j in range(2,len(arr)):
            sum += arr[j]
            operation += sum
        print("Total sum:", end=" ")
        print(sum)
        print("Total operation:", end=" ")
        print(operation)

    print("-----------------------------------------------") 


def Driver():
    FirstQ()
    SecondQ()
    ThirdQ()
    FourthQ()
    FifthQ()

Driver()