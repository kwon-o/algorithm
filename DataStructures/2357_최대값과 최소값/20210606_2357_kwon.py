a = open("input.txt", "r")

N, M = map(int, a.readline().split())

N_list = []
for _ in range(N):
    N_list.append(int(a.readline()))

for _ in range(M):
    a, b = map(int, a.readline().split())

