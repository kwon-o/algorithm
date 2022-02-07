from collections import deque
import heapq
import sys

N = int(input())
shop = deque(map(int,input().split()))
person = int(input())
check = int(N/person)
shop_sort = []
result = []

for i in range(person):
    for j in range(check):
        heapq.heappush(shop_sort, shop.popleft())
    for k in range(check):
        result.append(heapq.heappop(shop_sort))
        
for i in result:
    print(i, end=' ')
