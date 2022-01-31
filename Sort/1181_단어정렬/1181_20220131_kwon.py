l=[]
for _ in range(int(input())):
	l.append(input())
l=list(set(l))
l=sorted(l, key=lambda x : (len(x), x))
for i in l:
	print(i)