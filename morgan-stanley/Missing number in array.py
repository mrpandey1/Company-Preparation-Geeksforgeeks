def ans(nums):
    ex_sum=((len(nums)+2)*(len(nums)+1))//2
    ac_sum=sum(nums)
    return ex_sum-ac_sum
a=int(input())
for i in range(a):
    b=int(input())
    c=list(map(int,input().strip().split()))[:b-1]
    print(ans(c))
