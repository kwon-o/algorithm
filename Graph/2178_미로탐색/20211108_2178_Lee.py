from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
# visited = []
# for i in range(N):
#     for j in range(M):
#         visited[i][j].append(False)
#
# visited[0][0].append(True)
visited = [[False]*M for _ in range(N)]
visited[0][0] = True
cnt = 0
deq = deque()
deq.append((0, 0))
dx = [0, 0, -1, 1] #상하좌우
dy = [-1, 1, 0, 0]

while deq:
    x, y = deq.popleft()

    for i in range(4):
        testX = x+dx[i]
        testY = y+dy[i]
        if testX < 0 or testY < 0 or testX >= N or testY >= M:
            continue
        if visited[testX][testY] or board[testX][testY] == 0:
            continue

        deq.append((testX, testY))
        board[testX][testY] = board[x][y] + 1
        visited[testX][testY] = True
print(board[N-1][M-1])
