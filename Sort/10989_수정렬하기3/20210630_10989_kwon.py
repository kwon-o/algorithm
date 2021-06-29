import sys
c=[0]*(10001)
for i in range(int(input())):
	n=int(sys.stdin.readline())
	c[n]=c[n]+1
for i in range(10001):
	if c[i]!=0:
		for _ in range(c[i]):
			print(i)