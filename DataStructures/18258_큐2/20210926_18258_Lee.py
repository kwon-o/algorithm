from collections import deque
import sys

n = int(input())
deq = deque()

for i in range(n):
    a = sys.stdin.readline().split()

    if a[0] == 'push':
        deq.append(a[1])
    elif a[0] == 'pop':
        if len(deq) >= 1:
            print(deq.popleft())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(deq))
    elif a[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if len(deq) >= 1:
            print(deq[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if len(deq) >= 1:
            print(deq[-1])
        else:
            print(-1)
