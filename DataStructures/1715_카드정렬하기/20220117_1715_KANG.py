
import heapq


n = int(input())
num = []

k=0

for _ in range(n):
    heapq.heappush(num, int(input()))
    
for i in range(n-1): 
    pop_num1 = heapq.heappop(num) 
    pop_num2 = heapq.heappop(num) 
    k += pop_num1 + pop_num2 
    heapq.heappush(num, pop_num1+pop_num2)
    
print(k)



