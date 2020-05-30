def maxSubArray(a):
        l1 =a[0] 
        l2 = a[0]
        for i in range(1,len(a)):
            l2 = max(a[i], l2 + a[i]) 
            l1 = max(l1,l2)
            print(l1,l2)
            print('----')
        return l1
print(maxSubArray([1,2,3,-2,-5]))
