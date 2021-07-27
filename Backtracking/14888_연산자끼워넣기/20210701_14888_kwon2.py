from itertools import permutations
import sys
input=sys.stdin.readline
N=int(input())
n=list(map(int,input().split()))
k=list(map(int,input().split()))
l=[]
Max=-987654321
Min=987654321
for h,i in enumerate(k):
	l.append([h]*i)
k=list(permutations(sum(l,[])))
for i in k:
	a=n[0]
	for h,j in enumerate(i):
		if j==0:
			a+=n[h+1]
		elif j==1:
			a-=n[h+1]
		elif j==2:
			a*=n[h+1]
		else:
			if a>0:
				a=a//n[h+1]
			else:
				a=-a
				a=a//n[h+1]
				a=-a
	Max=max(a,Max)
	Min=min(a,Min)
print(Max)
print(Min)