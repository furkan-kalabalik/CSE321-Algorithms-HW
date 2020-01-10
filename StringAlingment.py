s2 = "algorithm"
s1 = "algoritma"

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
print(dp[len(s1)][len(s2)])
print(a1)
print(a2)