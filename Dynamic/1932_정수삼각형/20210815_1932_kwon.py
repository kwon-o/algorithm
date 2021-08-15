n=int(input())
l=[]
for _ in range(n):
    l.append(list(map(int, input().split())))
m=l
for i in range(1,n):
    for j in range(i+1):
        if j==0:
            a=0
        else:
            a=l[i-1][j-1]+l[i][j]
        if j==i:
            b=0
        else:
            b=l[i-1][j]+l[i][j]
        if a>b:
            m[i][j]=a
        else:
            m[i][j]=b
print(max(m[n-1]))