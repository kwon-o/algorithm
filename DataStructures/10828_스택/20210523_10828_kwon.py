from sys import stdin
steck = []
for _ in range(int(stdin.readline())):
	inp = stdin.readline().split()
	if inp[0]=='push':
		steck.append(int(inp[1]))
	elif inp[0]=='pop' and len(steck)>0:
		print(steck.pop())
	elif inp[0]=='pop' and len(steck)==0:
		print(-1)
	elif inp[0]=='size':
		print(len(steck))
	elif inp[0]=='empty' and len(steck)>0:
		print(0)
	elif inp[0]=='empty' and len(steck)==0:
		print(1)
	elif inp[0]=='top' and len(steck)>0:
		print(steck[len(steck)-1])
	elif inp[0]=='top' and len(steck)==0:
		print(-1)