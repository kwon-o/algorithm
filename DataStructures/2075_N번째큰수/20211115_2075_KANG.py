import heapq
import sys

N = int(input())

heap = []

for _ in range(N):
    matrix = list(map(int,sys.stdin.readline().split()))

    if not heap: 
        for a in matrix:
            heapq.heappush(heap,a)       
    else:
        for a in matrix:
            print(heap[0], a)
            if heap[0] < a:
                heapq.heappush(heap,a)
                heapq.heappop(heap)
            print(heap)
    
print(heap[0])