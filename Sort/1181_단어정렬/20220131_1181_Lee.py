N = int(input())
arry = []

for i in range(N):
    alpha = input()
    arry.append((len(alpha), alpha))

result = list(set(arry))

result.sort()
for i in range(len(result)):
    print(result[i][1])
