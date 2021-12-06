import sys
from collections import deque

N = int(sys.stdin.readline())
temp = deque()
for i in range(N):
    bro = int(sys.stdin.readline())
    min = 0
    max = i - 1
    while min <= max:
        idx = int((min + max) / 2)
        mid = temp[idx]
        if mid < bro:
            min = idx + 1
        elif mid > bro:
            max = idx - 1
        else:
            min = idx
            break
    temp.insert(min, bro)
    print(temp[int(i / 2)])
