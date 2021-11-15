import heapq
N = int(input())
heap = []

for _ in range(N):
    il = list(map(int, input().split()))

    if not heap:
        for i in il:
            heapq.heappush(heap, i)
    else:
        for i in il:
            if heap[0] < i:
                heapq.heappush(heap, i)
                heapq.heappop(heap)

print(heap[0])