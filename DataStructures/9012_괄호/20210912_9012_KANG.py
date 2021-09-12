
n = int(input())
answer =[]
for i in range(n):
    h = input()
    s = list(h)
    check = 0
    for i in s:
        if i == '(':
            check += 1
        elif i == ')':
            check -= 1
        if check < 0:
            answer.append("NO")
            break
    if check > 0:
        answer.append("NO")
    elif check == 0:
        answer.append("YES")

for k in answer:
     print(k)




