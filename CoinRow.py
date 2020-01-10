C = [0,1, 3, 4, 11, 3, 9]
def CoinRow(coins):
    F = []
    F.append(0)
    F.append(coins[1])    
    for i in range(2, len(coins)):
        F.append(max(C[i]+F[i-2], F[i-1]))
    return F[len(coins)-1]

print (CoinRow(C))