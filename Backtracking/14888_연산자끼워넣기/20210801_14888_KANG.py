from itertools import permutations


sa = ['+','-','*','/']
N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
salist=[]

for i in range(4):
    for j in range(B[i]):
        salist.append(sa[i])
B =list(permutations(salist))

answer = []

for i in B:
    x = A[0]
    for j in range(len(A)-1):
        if i[j]=='+':
            x += A[j+1]
        elif i[j]=='-':
            x -= A[j+1]
        elif i[j]=='*':
            x *= A[j+1]
        else:
            if x//A[j+1] <0:
                x = -(-x//A[j+1])
            else:
                x = x//A[j+1]
 
    answer.append(x)

print(max(answer))
print(min(answer))


