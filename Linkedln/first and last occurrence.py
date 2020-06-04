def ans(a,k):
    left,right=0,len(a)-1
    flag=0
    while left<=right:
        mid=int((left+right)//2)
        if a[mid]==k:
            ptr1=ptr2=mid
            flag=1
            while ptr1>0 and ptr2<len(a)-1:
                if a[ptr1-1]==k:
                    ptr1-=1
                if a[ptr2+1]==k:
                    ptr2+=1
                if a[ptr2+1]!=k and a[ptr1-1]!=k:
                    break
            break
        elif a[mid]>k:
            right=mid-1
        else:
            left=mid+1

    if flag==0:
        print(-1)
    else:
        print(ptr1,ptr2)
for i in range(int(input())):
    a=int(input())
    b=list(map(int,input().strip().split()))[:a]
    target=int(input())
    ans(b,target)
