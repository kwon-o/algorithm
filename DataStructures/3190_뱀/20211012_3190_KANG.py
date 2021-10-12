from collections import deque

N = int(input())  #보드크기
K = int(input())  #사과위치

time= 0
snake = deque()
snake.append((0,0)) #뱀초기위치 저장


board = [[0 for col in range(N)] for row in range(N)] #보드크기설정

board[0][0]=2  #보드의 가장 첫번째 칸에 뱀을 둠

for _ in range(K):
    a,b = map(int, input().split()) 
    board[a-1][b-1] = 1  #사과위치저장

L = int(input())    #뱀방향정보 저장
L_board = ([input().split() for _ in range(L)])

x=0
y=0
LA=0

while(True):
    time +=1
    if (x==N or y ==N or x<0 or y<0):
        break;   
    if board[x][y] == 1: #사과있음
            snake.append([x,y])
            board[x][y] == 0
            y+=1
    elif board[x][y] == 0: #사과없음
            snake.append([x,y])
            pop_x, pop_y = snake.popleft()
            board[pop_x][pop_y] == 0
            y+=1
    elif (x+y>0):
        if(board[x][y] == 2):#게임종료
            # print(x,y)
            break;
    if(len(L_board)>LA):
        if(int(L_board[LA][0])==time):
            if(L_board[LA][1]=="L"): #왼쪽
                x-=1
            elif(L_board[LA][1]=="D"): #오른쪽
                x+=1
            LA+=1  

print(time)