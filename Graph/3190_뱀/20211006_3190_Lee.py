import sys
from collections import deque

deq = deque()
boardNum = int(input())
appleNum = int(input())
# board = []
# for i in range(boardNum):
#     for j in range(boardNum):
#         board[i][j] = 0
# board = [[0 for col in range(boardNum)] for row in range(boardNum)]
# print(board)
apple = []
for i in range(appleNum):
    apple.append(list(map(int, input().split())))

wayNum = int(input())
way = {}
for i in range(wayNum):
    temp = sys.stdin.readline().split()
    way[int(temp[0])] = temp[1]
    print(way)

time = 0
head = [1, 1]
tail = deque()
left = [[0, 1], [-1, 0], [0, -1], [1, 0]]
right = [[0, 1], [1, 0], [0, -1], [-1, 0]]
direction = [0, 1]
order = 0

while True:
    #방향전환(언제 어디로전환)
    if time in way:
        if way[time] == "L":
            order = left.index(direction)
            if order + 1 == 4:
                direction = left[0]
            else:
                direction = left[order + 1]
        elif way[time] == "D":
            order = right.index(direction)
            if order + 1 == 4:
                direction = right[0]
            else:
                direction = right[order + 1]
    print(order)
    head = [head[0] + direction[0], head[1] + direction[1]]
    #사과 먹을경우
    if head in apple :
        time += 1
        tail.appendleft(head)
        #사과 지우기

    # 사과 안먹을경우 (이동가능한지 확인)
    else:
        time += 1
        if head[0] < 0 or head[1] < 0 or head[0] > boardNum or head[1] > boardNum or head in tail:
            print(time)
            exit
        tail.appendleft(head)
        tail.pop()



