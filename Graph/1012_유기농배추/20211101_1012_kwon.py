from collections import deque

for _ in range(int(input())):
    M, N, K = map(int,input().split())
    Map = [[0] * M for _ in range(N)]
    for _ in range(K):
        by, bx = map(int,input().split())
        Map[bx][by] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    ans = 0

    for i in range(N):
        for j in range(M):
            if Map[i][j] == 0:
                continue
            else:
                Map[i][j] = 0
                ans += 1
                q = deque()
                q.append((j, i))
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < M and 0 <= ny < N and Map[ny][nx] == 1:
                            Map[ny][nx] = 0
                            q.append((nx, ny))

    print(ans)