from collections import deque
from sys import stdin

for _ in range(int(stdin.readline())):
	N, M = map(int, stdin.readline().split())
	queue = deque(map(int, stdin.readline().split()))
	ans = 0
	while True:
		if queue[0] == max(queue):
			queue.popleft()
			ans += 1
			if M == 0:
				print(ans)
				break
			else:
				M -= 1
		else:
			queue.append(queue.popleft())
			if M == 0:
				M = len(queue)-1
			else:
				M -= 1