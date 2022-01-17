import heapq
import sys
p=sys.stdin.readline
h=[]
for _ in range(int(p())):
    i=int(p())
    if i==0:
        if len(h)==0:print(0)
        else:print(heapq.heappop(h)[1])
    else:heapq.heappush(h,(abs(i), i))