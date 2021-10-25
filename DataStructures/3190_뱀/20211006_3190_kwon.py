from collections import deque
snake = deque()

N = int(input())
apple = []
for _ in range(int(input())):
    apple.append(list(map(int, input().split())))
rotationDic = {}
for _ in range(int(input())):
    l = list(input().split())
    rotationDic[int(l[0])] = l[1]

headLocation = [1, 1]
snake.append([1, 1])
direction = 'right'
anw = 0


def rotation(ro, lf):
    if ro == 'right':
        if lf == 'L':
            newDirection = 'up'
        else:
            newDirection = 'down'
    elif ro == 'left':
        if lf == 'L':
            newDirection = 'down'
        else:
            newDirection = 'up'
    elif ro == 'up':
        if lf == 'L':
            newDirection = 'left'
        else:
            newDirection = 'right'
    else:
        if lf == 'L':
            newDirection = 'right'
        else:
            newDirection = 'left'
    return newDirection


while True:
    anw += 1

    if direction == 'right':
        headLocation[1] += 1
    elif direction == 'left':
        headLocation[1] -= 1
    elif direction == 'up':
        headLocation[0] -= 1
    else:
        headLocation[0] += 1

    if headLocation[0] < 1 or headLocation[1] < 1 or headLocation[0] > N or headLocation[1] > N or headLocation in snake :
        print(anw)
        break
    else:
        snake.append(headLocation.copy())
        if headLocation not in apple:
            snake.popleft()
        else:
            apple.remove(headLocation)

    if anw in rotationDic.keys():
        direction = rotation(direction, rotationDic[anw])