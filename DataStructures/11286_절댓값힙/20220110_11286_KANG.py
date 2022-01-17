import sys
import heapq

input = sys.stdin.readline
heap = []

x = input()
x = int(x)

for _ in range(x):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        if(len(heap)==0):
            print(0)
        else:
            print(heapq.heappop(heap)[1])