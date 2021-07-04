N=int(input())
for i in range(max(0,N-len(str(N))*9),N):
	a=i+sum([int(j) for j in str(i)])
	if a==N:
		print(i)
		exit()
print(0)