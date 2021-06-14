for i in list(input()):
	c=0
	for j in list(str(ord(i))):
		c+=int(j)
	print(i*c)