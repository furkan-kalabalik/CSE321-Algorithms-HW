arr = [3, 13, 7, 5, 21, 23, 23, 40, 23, 14, 12, 56, 23, 29]

def split(liste, pivot, left, right):
    for i in range(1,len(liste)):
        if liste[i] > pivot:
            right.append(liste[i])
        else:
            left.append(liste[i])

def print_list(liste):
    for i in liste:
        print(i, end=' ')
    print("\n")

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

def find_median(liste):
    if(len(liste) % 2 == 1):
        return find_kth(liste, (len(liste)/2) + 1)
    else:
        return 0.5 * (find_kth(liste, len(liste)/2) + find_kth(liste, len(liste)/2 + 1))

print(find_median(arr))