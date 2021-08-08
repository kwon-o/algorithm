import heapq
from operator import itemgetter

N = int(input())

A=[]
for i in range(N):
    A.append(list(map(int, input().split())))

A.sort(key =itemgetter(1))

# B=A[0][0]
# C = 0
# print(B)
# while(C<N):
#     K=[0][C]
#     for i in range(N):
#         if(K<N[i][C])
        
    
#     B = B+K
#     C+=1
# for i in A:
#     print(i[0])
    
B =[]
for i in A:
  heapq.heappush(B, i[0])
  if (len(B)>i[1]):
    heapq.heappop(B)

print(sum(B))