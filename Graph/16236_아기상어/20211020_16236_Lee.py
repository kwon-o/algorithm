from collections import deque

n = int(input())
sharkSize = 2
sharkNow = deque()
fishNow = deque()
fishSize = deque()
time = 0


board = [list(map(int, input().split())) for _ in range(n)]

#상어 위치, 물고기 위치, 물고기 크기
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            sharkNow.append([i, j])
        elif board[i][j] != 0:
            fishNow.append([i, j, 0])
            fishSize.append(board[i][j])

#물고기가 한마리일 경우는 상어보다 작으면 먹고, 시간은 물고기 위치까지 간거리, 물고기 제거, 종료)
# if len(fishNow) == 1 and sharkSize > fishSize[0]:
#     time = abs(sharkNow[0][0] - fishNow[0][0]) + abs(sharkNow[0][1] - fishNow[0][1])
#     fishSize.pop()
#     fishNow.pop()
#     print(time)
# else:
fish = []
fishCnt = 0
if len(fishNow) == 0:
    print(time)

fishMin = 6
for i in range(len(fishNow)):
    fishNow[i][2] = abs(sharkNow[0][0] - fishNow[i][0]) + abs(sharkNow[0][1] - fishNow[i][1])
    if fishMin > fishNow[i][2]:
        fishMin = fishNow[i][2]
    #(*)상어보다 작고 가까운 물고기 파악
    # 물고기가 많으면 젤 위 물고기, 그래도 많으면 젤 왼쪽 물고기
i = 0
while len(fishNow) > 0:
    if sharkSize > fishSize[i] and fishMin == fishNow[i][2]:
        fish.append(fishNow[i])
        # 물고기 먹기 (시간 = 물고기 위치까지 간거리, 상어 위치 변경 = 물고기 먹은 장소, 물고기 제거하기, 물고기 카운트== 상어크)
        if len(fish) > 1:
            fish.sort()
            idx = fishNow.index(fish[0])
            del fishSize[idx]
            # fishSize.pop(1)
            time = time + fishNow[i][2]
            sharkNow.pop()
            sharkNow.append(fish[0])
            fishNow.remove(fish[0])
            fishCnt += 1
            fish.clear()
            i = 0
            if fishCnt == sharkSize:
                sharkSize += 1
                fishCnt = 0
        elif len(fish) == 1:
            time = abs(sharkNow[0][0] - fishNow[0][0]) + abs(sharkNow[0][1] - fishNow[0][1])
            fishSize.pop()
            fishNow.pop()
            i += 1
            if len(fishSize) == 0:
                print(time)
                exit
    else:
        fishMin += 1
        #물고기 없을때, 물고기가 상어보다 큰거밖에 없을때 끝내기 (시간 출력)
    if len(fishNow) == 0:
        print(time)
        exit()
    if len(fishNow) == 1 and sharkSize < fishSize[0]:
        print(time)
        exit()
    i += 1
