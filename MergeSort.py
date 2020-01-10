A = [9, 6, 7, 19, 2]
def MergeSort(arr, l, r):
    if r-l+1 > 1:
        mid = (r+l)//2
        arr1 = arr[l:mid+1]
        arr2 = arr[mid+1:r+1]
        r1,arr1 = MergeSort(arr1,0, len(arr1)-1)
        r2,arr2 = MergeSort(arr2,0, len(arr2)-1)
        return merge(arr,arr1,arr2,r1+r2)
    else:
        return 0,arr

def merge(arr,arr1,arr2,inv):
    k = 0
    i = 0
    j = 0
    while(i < len(arr1) and j < len(arr2)):
        if(arr1[i] < arr2[j]):
            arr[k] = arr1[i]
            i = i+1
        else:
            arr[k] = arr2[j]
            inv = inv+len(arr1)-i
            j = j+1
        k = k+1
    if (i == len(arr1)):
        while(k < len(arr)):
            arr[k] = arr2[j]
            j = j+1
            k = k+1
    else:
        while(k < len(arr)):
            arr[k] = arr1[i]
            i = i+1
            k = k+1
    return inv, arr

print(MergeSort(A,0,len(A)-1))
