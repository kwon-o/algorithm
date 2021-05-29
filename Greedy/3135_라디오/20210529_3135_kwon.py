A,B=map(int,input().split())
result=abs(A-B)
for _ in range(int(input())):
    N=abs(B-int(input()))
    if result>N:result=N+1
print(result)