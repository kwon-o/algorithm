from collections import deque

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]  


shark_x, shark_y = 0,0
for i in range(n):
    for j in range(n):
        if  board[i][j] == 9:
             shark_x, shark_y = i,j

board[shark_x][shark_y]=0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def BFS(s_x, s_y):
    visit = [[0] * n for i in range(n)]
    visit[s_x][s_y] =1

    queue = deque()
    queue.append(s_x,s_y)
    while queue:
        x,y= queue.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <=nx < n and 0 <= ny  <n and visit[nx][ny] ==0:

        
       












