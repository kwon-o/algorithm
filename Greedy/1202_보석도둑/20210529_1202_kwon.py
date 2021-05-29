from sys import stdin
import heapq

N, K = map(int, stdin.readline().split())
jewelryArr = []
bagArr = []
for _ in range(N):
    heapq.heappush(jewelryArr, list(map(int, stdin.readline().split())))
for _ in range(K):
    bagArr.append(int(stdin.readline()))
jewelryArr.sort(key=lambda x : x[0])
bagArr.sort()

ans = 0
ansArr = []
for bag in bagArr:
    while jewelryArr and bag >= jewelryArr[0][0]:
        heapq.heappush(ansArr, -heapq.heappop(jewelryArr)[1])
    if ansArr:
        ans -= heapq.heappop(ansArr)
    elif not jewelryArr:
        break
print(ans)