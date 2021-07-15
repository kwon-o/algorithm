for _ in range(int(input())):
	l=list(input())
	c=0
	a=0
	for i in l:
		if i=='O':
			c+=1
			a+=c
		else:
			c=0
	print(a)