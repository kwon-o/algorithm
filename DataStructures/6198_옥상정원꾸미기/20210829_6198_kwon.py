n=int(input())
s=[]
c=0
for i in range(n):
    t=int(input())
    while s!=[] and s[-1] <= t:
        s.pop()
    c+=len(s)
    s.append(t)
print(c)