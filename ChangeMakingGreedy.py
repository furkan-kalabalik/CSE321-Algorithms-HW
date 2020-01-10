C = [25,10,5,1]


def ChangeMakingGreedy(coins, amount):
    total = 0
    for i in coins:
        while(amount >= i):
            amount = amount - i
            total = total+1
    return total

print(ChangeMakingGreedy(C,48))