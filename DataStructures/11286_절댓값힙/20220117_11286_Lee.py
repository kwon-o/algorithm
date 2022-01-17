import heapq
import sys

nums = int(input())
heap = []
for i in range(nums):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) >= 1:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(num), num))
