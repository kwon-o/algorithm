import heapq
import sys

N = int(input())
dasom = int(input())
heap = []
a = 0
if N == 1:
    print(0)
else:
    for i in range(N-1):
        num = int(input())
        heapq.heappush(heap, (-num, num))

    while dasom <= heap[0][1]:
        a += 1
        dasom += 1
        b = heapq.heappop(heap)[1] - 1
        heapq.heappush(heap, (-b, b))
    print(a)
