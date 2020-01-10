A = [9, 6, 7, 19, 2]

def findLargest(arr, l, r):
    if(r == l):
        return arr[l]
    else:
        mid = (l+r)//2
        one = findLargest(arr,l,mid)
        two = findLargest(arr, mid+1, r)
        if(two >= one):
            return two
        else:
            return one

print(findLargest(A,0,len(A)-1))