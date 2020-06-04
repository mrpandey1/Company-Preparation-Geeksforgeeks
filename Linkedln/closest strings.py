def ans(s, w1, w2):
    s=s.split()
    print(w2)
    if w1==w2:
        return 0
    pos=0
    for i in range(len(s)):
        print(s[i])
        if s[i]==w1:
            pos=i
            break
    print(pos)
    for i in range(len(s)):
        if s[i]==w2:
            return abs(pos-i)
ans('the quick brown fox quick','fox','the')
"""
for i in range(int(input())):
    a=int(input())
    b=input()
    c=list(map(str,input().strip().split()))
    print(ans(b,c[0],c[1]))

"""
