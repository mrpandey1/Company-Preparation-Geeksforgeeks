def ans(a):
    new=[]
    for i in a:
        if i==0:
            new.insert(0,0)
        if i==1:
            new.append(1)
    for i in a:
        if i==2:
            new.append(2)
    print(new)
ans([0,2,1,2,0])
