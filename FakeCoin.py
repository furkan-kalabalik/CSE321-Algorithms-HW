arr = [1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1]

def print_list(liste):
    for i in liste:
        print(i, end=' ')
    print("\n")

def fakeCoin(liste):
    return fakeCoinHelper(liste, 0, len(liste) - 1)

def findSum(liste, pos1, pos2):
    sum = 0
    for i in range(pos1,pos2):
        sum += liste[i]
    return sum

def fakeCoinHelper(liste, start, end):
    len_list = end-start+1
    if(len_list % 2 == 0):
        if(len_list == 2):
            if(liste[start] < liste[end]):
                return start
            else:
                return end
        firstHalf = findSum(liste, start, start+(len_list//2))
        secondHalf = findSum(liste, start+(len_list//2), end + 1)
        if(firstHalf > secondHalf):
            return fakeCoinHelper(liste, start+(len_list//2), end)
        else:
            return fakeCoinHelper(liste, start, start+(len_list//2)-1)
    else:
        len_list = end-start+1
        if(len_list == 3):
            if(liste[start] < liste[end-1]):
                return start
            elif (liste[start] > liste[end-1]):
                return end - 1
            else:
                return end
        firstHalf = findSum(liste, start, start+(len_list//2))
        secondHalf = findSum(liste, start+(len_list//2), end)
        if(firstHalf > secondHalf):
            return fakeCoinHelper(liste, start+(len_list//2), end)
        elif (firstHalf == secondHalf):
            return end
        else:
            return fakeCoinHelper(liste, start, start+(len_list//2))
print(fakeCoin(arr))