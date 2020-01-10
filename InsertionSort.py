arr3 = [1, 3, 2]
arr = [1, 6, 9, 4, 3, 7, 8, 2]
arr2 = [1, 6, 9, 4, 3, 7, 8, 2, 24, 20, 34, 12, 41, 11]
count = 0
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

def swap(liste, position1, position2):
    temp = liste[position1]
    liste[position1] = liste[position2]
    liste[position2] = temp

def QuickSort(arr):
    QuickHelper(arr, 0, len(arr)-1)

def QuickHelper(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        QuickHelper(arr, l, s-1)
        QuickHelper(arr, s+1, r)

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

arr = [1, 6, 9, 4, 3, 7, 8, 2]
arr2 = [1, 6, 9, 4, 3, 7, 8, 2, 24, 20, 34, 12, 41, 11]
arr3 = [1, 3, 2]

print(arr[:])

