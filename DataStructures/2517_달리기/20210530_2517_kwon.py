import heapq
N,*l=map(int,open("input.txt", "r").read().split())
heap=[]
for i, n in enumerate(l):
    heapq.heappush(heap, (i,n))
for i in heap:
    ans=1
    for j in range(i[0]):
        if i[1] <= heap[j][1]:
            ans+=1
    print(ans)