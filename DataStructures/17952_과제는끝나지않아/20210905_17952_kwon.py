import sys
i=sys.stdin.readline
N=int(i())
s=[]
r=0
for _ in range(N):
    a=list(map(int,i().split()))
    if a[0]==1:
        a[2]-=1
        s.append(a)
    elif s==[] and a[0]==0:continue
    else:
        s[-1][2]-=1
    if s[-1][2]==0:
        r+=s[-1][1]
        s.pop()
print(r)