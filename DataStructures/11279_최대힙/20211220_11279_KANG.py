import sys
import heapq

input = sys.stdin.readline
heap = []

N = int(input())

for _ in range(N):
    k= int(input())
    if(k==0):
        if(len(heap)==0):
            print(0)
        else:
            ttt =-heapq.heappop(heap)
            print(ttt)
    else:
        heapq.heappush(heap, -k)
    

