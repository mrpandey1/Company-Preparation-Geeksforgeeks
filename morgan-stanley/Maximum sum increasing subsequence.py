def ans(a):
    max=0
    temp=[0 for i in range(len(a))]
    for i in range(len(a)):
        temp[i]=a[i]
    for i in range(1,len(a)):
        for j in range(i):
            if (a[i]>a[j] and temp[i]<temp[j]+a[i]):
                temp[i]=temp[j]+a[i]
    for i in range(len(a)):
        if max<temp[i]:
            max=temp[i]
    return max
print(ans([1,101,2,3,100,4,5]))
