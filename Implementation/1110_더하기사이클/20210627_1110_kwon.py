n=input()
m=int(n)
a=0
while True:
	if len(n)==1:
		n='0'+n
	n=n[-1]+str(int(n[0])+int(n[1]))[-1]
	a+=1
	if int(n)==m:
		break
print(a)