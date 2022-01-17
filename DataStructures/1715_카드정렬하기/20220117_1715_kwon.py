from heapq import *
l=[]
for _ in range(int(input())):
    heappush(l,int(input()))
a=0
while len(l)>1:
    t=heappop(l)+heappop(l)
    a+=t
    heappush(l,t)
print(a)