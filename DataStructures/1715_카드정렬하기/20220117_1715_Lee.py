import heapq

N = int(input())

card = []
for i in range(N):
    num = int(input())
    heapq.heappush(card, num)

sum = 0
while len(card) > 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    heapq.heappush(card, a+b)
    sum = sum + (a+b)
print(sum)
