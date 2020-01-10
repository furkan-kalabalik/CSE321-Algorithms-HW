memo = [None, None, None, None, None,None]

def fiboMemo(n, memo):
    if(memo[n] != None):
        return memo[n]
    if(n == 1 or n == 2):
        result = 1
    else:
        result = fiboMemo(n-1,memo) + fiboMemo(n-2, memo)
    memo[n] = result
    return result

print(fiboMemo(6, memo))