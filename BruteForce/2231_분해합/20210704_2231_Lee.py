n = int(input())
for i in range(1, n):
    aaa = i
    num = i
    while True:
        aaa += num % 10
        num = num // 10
        if num == 0:
            break
    if aaa == n:
        print(i)
        exit()
print(0)
