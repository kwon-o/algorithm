import heapq
l=[list(map(int,input().split()))for _ in range(int(input()))]
l.sort(key=lambda x:(x[1]))
m=[]
for i,j in l:
    heapq.heappush(m,i)
    print(m)
    if len(m)>j:
        heapq.heappop(m)
        print(m)
print(sum(m))