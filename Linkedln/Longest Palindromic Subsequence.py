def ans(a,b,n):
    l=[[0 for i in range(n+1)]for j in range(n+1)]
    for i in range(0,n+1):
        for j in range(0,n+1):
            if i==0 or j==0:
                l[i][j]=0
            elif a[i-1]==b[j-1]:
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
    for i in l:
        for j in i:
            print(i[j],end=' ')
        print()
    return l[n][n]
for i in range(int(input())):
    a=input()
    print(ans(a,a[::-1],len(a)))
