from sys import stdin
N = int(stdin.readline())
crane = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
boxs = list(map(int, stdin.readline().split()))
crane.sort(reverse=True)
boxs.sort(reverse=True)
if boxs[0]>crane[0]:
    print(-1)
    exit()
ans=0
while boxs:
    i=0
    cnt=0
    j=0
    while j<N and i<len(boxs):
        if boxs[i]<=crane[j]:
            cnt+=1
            j+=1
            del boxs[i]
        else:
            i+=1
        if cnt==N:
            break
    if cnt<N:
        N=cnt
    ans+=1
print(ans)