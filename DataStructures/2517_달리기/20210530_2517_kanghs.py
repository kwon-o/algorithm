
from sys import stdin
mans = int(stdin.readline()) 

ability= []
answer = list(i+1 for i in range(mans))

# print(answer)
for i in range(mans):
    ability.append(int(stdin.readline()) )

for k in range(mans):
    j=k
    if k==0:
        continue
    else:
        while(j>0):
            if(ability[j-1]<ability[k]):
                answer[k]-=1;
            j-=1;

# print(answer)

for g in answer:
     print(g)




