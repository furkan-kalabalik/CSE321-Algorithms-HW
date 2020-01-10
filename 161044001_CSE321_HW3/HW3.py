boxes = ['B','B','B','B','W','W','W','W']
coins = [1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1]
median = [3, 13, 7, 5, 21, 23, 23, 40, 23, 14, 12, 56, 23, 29]
arr3 = [1, 3, 2]
arr = [1, 6, 9, 4, 3, 7, 8, 2]
arr2 = [1, 6, 9, 4, 3, 7, 8, 2, 24, 20, 34, 12, 41, 11]
count = 0
A = [2, 4, 7, 5, 22, 11]

"""Insertion Sort Function"""
def InsertionSort(arr):
    count = 0
    for i in range(1,len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and current < arr[j]:
            arr[j+1] = arr[j]
            count = count + 1
            j = j -1
        arr[j+1] = current
    return count

"""Quick Sort Main Function"""
def QuickSort(arr):
    QuickHelper(arr, 0, len(arr)-1)

"""Quick Sort Helper Function"""
def QuickHelper(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        QuickHelper(arr, l, s-1)
        QuickHelper(arr, s+1, r)

"""Partition for QuickSort"""
def partition(arr, l, r):
    pivot = arr[l]
    global count
    i = l + 1
    j = r
    flag = 1
    while flag:
        while i <= j and arr[i] <= pivot:
            i = i + 1
        while arr[j] >= pivot and j >= i:
            j = j - 1
        if j < i:
            flag = 0
        else:
            swap(arr, i ,j)
            count = count + 1   
    swap(arr, j, l)
    count = count + 1
    return j

"""Swap to list elements"""
def swap(liste, position1, position2):
    temp = liste[position1]
    liste[position1] = liste[position2]
    liste[position2] = temp

"""Prints List"""
def print_list(liste):
    for i in liste:
        print(i, end=' ')
    print("\n")

"""Alternating boxes helper function"""
def alternate_helper(liste, pos1, pos2):
    list_len = pos2 - pos1 + 1
    if(list_len == 2):
        return liste
    if (list_len == 4):
        swap(liste, pos1+1, pos2-1)
        return liste
    swap(liste, pos1+1, pos2-1)
    return alternate_helper(liste, pos1+2, pos2-2)
"""Alternating boxes main function"""
def alternate(liste):
    return alternate_helper(liste, 0, len(liste) - 1)

"""Find the sum of array from starting index to stop index """
def findSum(liste, pos1, pos2):
    sum = 0
    for i in range(pos1,pos2):
        sum += liste[i]
    return sum

"""Fake coin problem main function"""
def fakeCoin(liste):
    return fakeCoinHelper(liste, 0, len(liste) - 1)

"""Fake coin problem helper function"""
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

"""Split method split list into two half according to pivot"""
def split(liste, pivot, left, right):
    for i in range(1,len(liste)):
        if liste[i] > pivot:
            right.append(liste[i])
        else:
            left.append(liste[i])

"""Finds the smallest kth element in list"""
def find_kth(liste, k):
    pivot = liste[0]
    left = []
    right = []
    split(liste, pivot, left, right)
    if k == len(left) +1:
        return pivot
    if k <= len(left):
        return find_kth(left, k)
    if k > len(left) + 1:
        return find_kth(right, k-(len(left) + 1))

"""Finds median of list"""
def find_median(liste):
    if(len(liste) % 2 == 1):
        return find_kth(liste, (len(liste)/2) + 1)
    else:
        return 0.5 * (find_kth(liste, len(liste)/2) + find_kth(liste, len(liste)/2 + 1))

"""Finds sum of list"""
def findSumAll(arr):
    total = 0
    for i in arr:
        total += i
    return total

"""Finds multiplication of list"""
def findMult(arr):
    total = 1
    for i in arr:
        total *= i
    return total

"""Finds the subset condition for a list"""
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

"""Finding optimal solution"""
def findSubset(setA):
    optimal = setA.copy()
    condition = findCond(setA)
    return generate_subB([], setA, 0, condition, optimal)

"""Generates subsets and returns optimal solution"""
def generate_subB(temp, setA, start,condition, optimal):
    if(findSumAll(temp) >= condition and findMult(temp) < findMult(optimal)):
        optimal = temp.copy()
    for i in range(start, len(setA)):
        temp.append(setA[i])
        optimal = generate_subB(temp, setA, i + 1, condition, optimal)
        temp.pop()
    return optimal

def driver(boxes, coins, median, arr, arr2, arr3, A):
    print("-----TEST FOR ALTERNATING BOX--------\n")
    print("Normal Order:")
    print_list(boxes)
    print("\n")
    print("Alternating Order:")
    print_list(alternate(boxes))
    print("\n")
    print("-----TEST FOR FAKE COIN PROBLEM--------\n")
    print("Coins: ")
    print_list(coins)
    print("\n")
    print("Fake coin at index:")
    print(fakeCoin(coins))
    print("\n")
    print("-----TEST FOR FINDING MEDIAN--------\n")
    print("Median finding list:")
    print_list(median)
    print("\n")
    print("Median of list: ")
    print(find_median(median))
    print("\n")
    print("----INSERTION SORT------\n")
    print(*arr, sep = " ")
    print("Number of swaps: ")
    print(InsertionSort(arr))
    print(*arr, sep = " ")
    print("\n")
    print(*arr2, sep = " ")
    print("Number of swaps: ")
    print(InsertionSort(arr2))
    print(*arr2, sep = " ")
    print("\n")
    print(*arr3, sep = " ")
    print("Number of swaps: ")
    print(InsertionSort(arr3))
    print(*arr3, sep = " ")
    arr = [1, 6, 9, 4, 3, 7, 8, 2]
    arr2 = [1, 6, 9, 4, 3, 7, 8, 2, 24, 20, 34, 12, 41, 11]
    arr3 = [1, 3, 2]

    print("----QUICKSORT------\n")
    global count
    print(*arr, sep = " ")
    QuickSort(arr)
    print("Number of swaps: ")
    print(count)
    print(*arr, sep = " ")
    print("\n")
    count = 0
    print(*arr2, sep = " ")
    QuickSort(arr2)
    print("Number of swaps: ")
    print(count)
    print(*arr2, sep = " ")
    print("\n")
    count = 0
    print(*arr3, sep = " ")
    QuickSort(arr3)
    print("Number of swaps: ")
    print(count)
    print(*arr3, sep = " ")
    print("--------FINDING OPTIMAL SUBSET---------")
    print("Optimal subset: ")
    print(findSubset(A), sep= " ")
driver(boxes, coins, median, arr, arr2, arr3, A)