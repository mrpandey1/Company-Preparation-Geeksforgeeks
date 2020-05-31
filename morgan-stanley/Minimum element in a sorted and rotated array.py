def ans(a,target):
    low,high=0,len(a)-1
    mid=int((low+high)//2)
    while low<high:
        if a[mid]>a[mid+1]:
            return a[mid+1]
        elif a[mid] > a[high]:
            low = mid + 1
        else:
            high = mid
        mid = int((low + high) / 2)
    return a[mid]
a=int(input())
for i in range(a):
    target=int(input())
    b=list(map(int,input().strip().split()))
    print(ans(b,target))
