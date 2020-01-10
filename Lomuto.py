A = [9, 6, 7, 19, 2]

def lomuto(arr, l, r):
    p = A[l]
    s = l
    for i in range(l+1, r+1):
        if(arr[i] < p):
            s  = s + 1
            swap(arr, s, i)
    swap(arr, l, s)
    return s

def swap(liste, s, i):
    temp = liste[s]
    liste[s] = liste[i]
    liste[i] = temp

def QuickSelect(arr, l, r, n):
    s = lomuto(arr,l,r)
    if(s == n):
        return arr[s]
    elif(s > l+n-1):
        return QuickSelect(arr, l, s-1, n)
    else:
        return QuickSelect(arr,s+1, r, n-1-s)
print(QuickSelect(A,0,len(A)-1, 2))
