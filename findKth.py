arr1 = [1,2,3]
arr2 = [4,5,6]
count = 0

def findKth(arr1, start1, end1, arr2, start2, end2, k):
    global count
    count = count + 1
    if end1 - start1 < 0:
        return arr2[start2 + k]
    if end2 - start2 < 0:
        return arr1[start1 + k]
    if k == 0:
        return min(arr1[k + start1], arr2[k + start2])
    arr1MidIndex = (start1 + end1) // 2
    arr2MidIndex = (start2 + end2) // 2
    arr1Mid = arr1[arr1MidIndex]
    arr2Mid = arr2[arr2MidIndex]
    
    if ((arr1MidIndex - start1) + (arr2MidIndex - start2) < k):
        if(arr1Mid > arr2Mid):
            return findKth(arr1, start1, end1, arr2, arr2MidIndex+1, end2, k - (arr2MidIndex-start2) -1)
        else:
            return findKth(arr1, arr1MidIndex+1, end1, arr2, start2, end2, k - (arr1MidIndex-start1) - 1)
    else:
        if(arr1Mid > arr2Mid):
            return findKth(arr1, start1, arr1MidIndex-1, arr2, start2, end2, k)
        else:
            return findKth(arr1, start1, end2, arr2, start2, arr2MidIndex-1, k)

print (findKth(arr1,0,len(arr1)-1, arr2, 0, len(arr2)-1,2))
print (count)
