def ans(n,arr):
    i=0
    while i < len(arr)-1:
        if arr[i]==arr[i+1]:
            del arr[i]
        else:
            i+=1
    return len(arr)
ans([1])
            
