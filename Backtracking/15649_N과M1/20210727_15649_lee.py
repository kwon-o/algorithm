from itertools import permutations

N = int(input())
M = int(input())
arr = []
for i in range(1, N+1):
    arr.append(i)
for p in permutations(arr, M):
    print(' '.join(map(str, p)))
