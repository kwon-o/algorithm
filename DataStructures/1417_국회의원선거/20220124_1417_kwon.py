from heapq import *
N=int(input())
D=int(input())
l=[]
a=0
if N>1:
    for _ in range(N-1):
        heappush(l,-int(input()))
    while 1:
        p=-heappop(l)
        if D<=p:
            p-=1
            D+=1
            heappush(l,-p)
            a+=1
        else:
            break
print(a)