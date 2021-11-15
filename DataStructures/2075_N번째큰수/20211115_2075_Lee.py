n = int(input())
first = list(map(int, input().split()))
sumArr = []
for i in range(n-1):
    board = list(map(int, input().split()))
    sumArr = first + board
    sumArr.sort(reverse=True)
    first = sumArr[:n]
# print(first)
# print(sumArr)
print(first[n-1])

# # a = sum(board, [])
# # a.sort(reverse=True)
# # print(a[n-1])
