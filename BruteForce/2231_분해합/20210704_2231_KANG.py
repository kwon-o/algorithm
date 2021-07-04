N = int(input())
a=[]
for i in str(N):
    a.append(i)
if(N<99):
    K=1
else:
    K = 9*len(str(N))
    K = N-K 
LS=[]
while(K<N):
    b=[]
    S=K
    j=0
    for i in str(K):
        b.append(i)
    while(j<len(b)):
        S=S+int(b[j])
        j+=1
    if(N==S):
        LS.append(K)
    K+=1
if(len(LS)==0):
    print(0)
else:
    print(min(LS))