test = int(input())

for _ in range(test):
    result = 0
    M, N, K = map(int, input().split())
    cabbage = [[0] * M for _ in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())
        cabbage[b][a] = 1

    for i in range(N):
        for j in range(M):
            vegi = False
            if cabbage[i][j] == 1:
                vagi = True
                cabbage[i][j] = 2
                result += 1
                break
        if vegi:
            break
    worm = True
    while worm:
        worm = False
        for x in range(N):
            for y in range(M):
                up = x - 1
                down = x + 1
                left = y - 1
                right = y + 1
                if cabbage[x][y] == 2:
                    if up > 0:
                        if cabbage[up][y] == 1:
                            cabbage[up][y] = 2
                            worm = True
                    if left > 0:
                        if cabbage[x][left] == 1:
                            cabbage[x][left] = 2
                            worm = True
                    if down < N:
                        if cabbage[down][x] == 1:
                            cabbage[down][x] = 2
                            worm = True
                    if right < M:
                        if cabbage[x][right] == 1:
                            cabbage[x][right] = 2
                            worm = True
    print(result)
