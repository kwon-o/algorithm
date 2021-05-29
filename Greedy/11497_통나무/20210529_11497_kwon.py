from sys import stdin

T = int(input())

for i in range(T):
    N = int(input())
    arr = list(map(int, stdin.readline().split()))
    arr.sort()
    result = 0

    result = max(result, abs(arr[0] - arr[1]))
    result = max(result, abs(arr[-1] - arr[-2]))

    for i in range(N - 2):
        result = max(result, abs(arr[i] - arr[i + 2]))
    print(result)