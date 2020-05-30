def ans(arr, n, sum):  
    sumi = arr[0] 
    start = 0 
    i = 1
    while i <= n: 
        while sumi > sum and start < i-1: 
            sumi = sumi - arr[start] 
            start += 1
        if sumi == sum:
            print(start+1, i) 
            return 
        if i < n: 
            sumi = sumi + arr[i] 
        i += 1
    print (-1) 
    return 
a=int(input())
for i in range(a):
    b=list(map(int,input().strip().split()))[:2]
    c=list(map(int,input().strip().split()))[:b[0]]
    ans(c,b[0],b[1])
