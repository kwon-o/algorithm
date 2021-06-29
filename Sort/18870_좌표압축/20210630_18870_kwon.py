N=int(input())
l=list(map(int,input().split()))
k=sorted(set(l))
k={k[i]:i for i in range(len(k))}
print(*[k[i] for i in l])