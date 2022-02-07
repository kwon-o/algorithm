n=int(input())
l=list(map(int,input().split()))
k=n//int(input())
a=[]
for i in range(0,n,k):a+=sorted(l[i:i+k])
print(*a)
