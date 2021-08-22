A = int(input())

B = list(map(int, input().split()))

C = []

for i in range(A):
    if i==0:
        C.append(B[i])
    elif B[i]>B[i-1]:
        C.append(B[i])

print(len(C))
