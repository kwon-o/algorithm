from collections import deque
N, M = map(int, input().split())
Map = []
for _ in range(N):
    l = input()
    nl = []
    for i in range(M):
        nl.append(int(l[i]))
    Map.append(nl)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((0, 0))
while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < M and 0 <= ny < N and Map[ny][nx] == 1:
            q.append((nx, ny))
            Map[ny][nx] += Map[y][x]

print(Map[N-1][M-1] + 1)
