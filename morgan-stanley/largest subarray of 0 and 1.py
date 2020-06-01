def ans(nums):
    counts = {0:-1}
    curcount=0
    maxlen=0
    for i in range(N):
        if nums[i]==0:
            curcount-=1
        else:
            curcount+=1
        if curcount in counts:
            maxlen=max((i-counts[curcount]),maxlen)
        else:
            counts[curcount]=i
    return maxlen
print(ans([0,1,1]))

'''
    j=0
    ans=0
    while j != len(a):
        count=0
        count1=0
        for i in range(j,len(a)):
            if a[i]==0:
                count+=1
            if a[i]==1:
                count1+=1
            if count==count1:
                ans=max(count*2,ans)
                if ans==len(a):
                    return ans
        j+=1
    return ans
print(ans([0,1,1]))
'''
