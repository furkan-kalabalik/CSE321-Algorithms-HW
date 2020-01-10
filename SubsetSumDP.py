S = [-1, 6, 4,-5]
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

for i in range(len(dp)):
    for j in range(len(dp[0])):
        print(dp[i][j], end=" ")
    print()

isEqual = False

for i in range(len(dp)):
    if(dp[i][-neg] == True):
        isEqual = True

if(isEqual):
    print(*subset)
else:
    print("No subset like that")