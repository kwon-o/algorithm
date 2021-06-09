for _ in range(int(input())):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    d=((x1-x2)**2+(y1-y2)**2)**0.5
    s=r1+r2
    m=abs(r1-r2)
    if d==0 and r1==r2:
        print(-1)
    elif m<d<s:
        print(2)
    elif d==m or d==s:
        print(1)
    else:
        print(0)