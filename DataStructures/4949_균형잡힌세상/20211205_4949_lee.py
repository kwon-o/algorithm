from collections import deque

while True:
    sentence = input()
    box = deque()
    flag = 0

    if sentence == '.':
        break
    for i in sentence:
        if i == "(" or i == "[":
            box.append(i)
        elif i == ")":
            if len(box) == 0 or box[-1] == "[":
                print("no")
                flag = 1
                break
            else:
                box.pop()
        elif i == "]":
            if len(box) == 0 or box[-1] == "(":
                print("no")
                flag = 1
                break
            else:
                box.pop()
    if flag == 0:
        if not box:
            print("yes")
        else:
            print("no")
