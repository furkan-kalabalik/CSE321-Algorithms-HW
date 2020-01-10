arr = [1, 3, 20, 4, 1, 0]
def LocalMinima(arr,start,end):
    length = end-start+1
    if(length == 1):
        return arr[start]
    if(length == 2):
        if(arr[start] > arr[end]):
            return arr[end]
        else:
            return arr[start]
    mid = start+end//2
    if(arr[mid] < arr[mid-1] and arr[mid] < arr[mid+1]):
        return arr[mid]
    if(arr[mid-1] < arr[mid]):
        return LocalMinima(arr,start,mid-1)
    else:
        return LocalMinima(arr,mid+1,end)

print(LocalMinima(arr,0,len(arr)-1))