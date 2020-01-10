C = [1, 3, 5]
amount = 9

def changeMake(coins, amount):
    F = []
    F.append(0)

    for i in range(1,amount+1):
        j = 0
        temp = amount
        while(j < len(coins) and i >= coins[j]):
            temp = min(F[i-coins[j]], temp)
            j = j + 1
        F.append(temp + 1)
    print(*F)
    return F[amount]

print(changeMake(C,amount))