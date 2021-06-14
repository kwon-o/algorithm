a=0
for i in range(1,int(input())+1):
	j=len(str(i))
	if j==1 or j==2:
		a+=1
	else:
		l=list(map(int,list(str(i))))
		if l[0]-l[1] == l[1]-l[2]:
			a+=1
print(a)