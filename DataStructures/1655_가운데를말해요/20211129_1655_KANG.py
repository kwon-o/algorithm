import sys
import heapq
input = sys.stdin.readline
n = int(input())


heap1 = [] #왼쪽
heap2 = [] #오른쪽

for i in range(n):
    
    k=int(input())
    if len(heap1)==len(heap2):
        heapq.heappush(heap1, -k)
    else:
        heapq.heappush(heap2, k)

    if len(heap1) >= 1 and len(heap2) >= 1 and heap1[0] * -1 > heap2[0]:
        max_heap = heapq.heappop(heap1) * -1
        min_heap = heapq.heappop(heap2)
        
        heapq.heappush(heap1, min_heap * -1)
        heapq.heappush(heap2, max_heap)

    print(heap1[0] * -1)   