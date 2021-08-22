n=int(input())
l=list(map(int,input().split()))
k=[0 for _ in range(n)]
for i in range(n):
    a=l[i]
    for j in range(i+1):
        if a>l[j] and k[i]<k[j]:
            print(a,l[j],k[i],k[j])
            k[i]=k[j]
    k[i]+=1
print(k)
print(max(k))