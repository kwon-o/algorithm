from collections import deque
N = int(input())
Map = []
sx, sy = 0, 0
for i in range(N):
    l = list(map(int, input().split()))
    Map.append(l)
    if 9 in l:
        sx, sy = i, l.index(9)
Map[sx][sy] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

size, ans, eat = 2, 0, 0

while True:
    q = deque()
    q.append((sx, sy, 0))
    visited = [[False] * N for _ in range(N)]
    m = 362
    eatFish = []
    while q:
        x, y, cnt = q.popleft()
        if cnt > m:
            break
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if Map[nx][ny] > size or visited[nx][ny]:
                continue
            if Map[nx][ny] != 0 and Map[nx][ny] < size:
                eatFish.append((nx, ny, cnt + 1))
                m = cnt
            visited[nx][ny] = True
            q.append((nx, ny, cnt + 1))

    if eatFish:
        eatFish.sort()
        x, y, move = eatFish[0][0], eatFish[0][1], eatFish[0][2]
        ans += move
        eat += 1
        Map[x][y] = 0
        if eat == size:
            size += 1
            eat = 0
        sx, sy = x, y
    else:
        break

print(ans)