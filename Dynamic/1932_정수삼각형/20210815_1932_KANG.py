n = int(input())
t = []
for i in range(n):
    t.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(t[i])):
        if j == 0:
            t[i][j] = t[i][j] + t[i - 1][j]
        elif i == j:
            t[i][j] = t[i][j] + t[i - 1][j - 1]
        else:
            t[i][j] += max(t[i - 1][j - 1], t[i - 1][j])
print(max(t[n - 1]))

