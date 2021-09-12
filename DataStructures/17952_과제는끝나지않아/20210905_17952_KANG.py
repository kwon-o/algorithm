from sys import stdin

stack = []
time = []
answer =[]

n = int(stdin.readline())
for i in range(n):
    h = list(map(int, stdin.readline().split()))
    if h[0] == 1:
        stack.append(h[1])
        time.append(h[2]) 

    if len(time) ==0:
      continue
    else:
       time[-1] -= 1 
       if time[-1] == 0:
            time.pop()
            answer.append(stack.pop())
print(sum(answer))