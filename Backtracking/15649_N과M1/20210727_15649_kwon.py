import itertools
N,M=map(int,input().split())
l=[*range(N)]
k=list(itertools.permutations(l,M))
for i in k:
	for j in i:
		print(j+1,end=' ')
	print()