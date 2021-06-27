N = input()
count = 1


if(int(N)<10):
    N="0"+N
K = sum(map(int, str(N)))
B = N[-1]
K = B+str(K)[-1]

while(int(N)!=int(K)):
    B = str(K)[-1]
    if(int(K)<10):
        K="0"+str(K)
    else:
        K = sum(map(int, str(K)))
    K = str(K)[-1]
    K = B+K
    count +=1
print(count)