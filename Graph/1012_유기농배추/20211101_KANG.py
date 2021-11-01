from collections import deque
 
t = int(input()) #테스트케이스 


dx = [0,0,1,-1]
dy = [1,-1,0,0]
 


for i in range(t): #테스트 케이스 만큼 반복
    n,m,k= map(int, input().split()) #가로 세로 갯수  
    a =0
    b =0
    board = [[0]*m for _ in range(n)]    #빈 보드를 만들고
    count =0      #한번 출력하고 초기화

    for i in range(k):             #갯수 만큼     
        x, y = map(int,input().split())   #좌표 입력받아서 
        board[x][y] =1                  #보드의 그 좌표에 배추표시
   

    for a in range(n):
        for b in range(m):
            if board[a][b] == 1:
                queue = deque() 
                queue.append((a,b))
                board[a][b] =0
                while queue:
                    e,f = queue.popleft()
                    for j in range(4):
                        nx = e + dx[j]
                        ny = f + dy[j]
                        if  nx <0 or ny < 0 or nx>=n  or ny>=m:
                            continue
                        if board[nx][ny]==1: 
                            board[nx][ny]=0
                            queue.append((nx,ny))
                count +=1
    print(count)





