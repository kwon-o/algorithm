import sys
from collections import deque

N = int(input())
Q = deque()
 
for _ in range(N):
    M = list(map(str, sys.stdin.readline().split()))
    if M[0]=='push':
        Q.append(M[1])
    elif M[0]=='pop':
        if Q:
            print(Q.popleft())
        else:
            print("-1")
    elif M[0]=='size':
        print(len(Q))
    elif M[0]=='empty':
        if len(Q)==0:
            print(1)
        else:
            print(0)
    elif M[0]=='front':
        if Q:
            print(Q[0])
        else:
            print("-1")
    elif M[0]=='back':
        if Q:
            print(Q[-1])
        else:
            print("-1")
