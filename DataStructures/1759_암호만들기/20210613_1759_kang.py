
from sys import stdin
from itertools import combinations  #f리스트에 있는 모든 조합을 구하기 위함

moum = ['a','e','i','o','u']
3 
L,C  =  map(int, input().split())

Cmoji =  list(map(str,input().split()))

ja_lst=[]
mo_lst=[]


for i in Cmoji:
    k=0
    for j in moum:
        if i==j:
           k=1;
    if k==1:
        ja_lst.append(i)
    else:
        mo_lst.append(i)


total=[]

for i in range(2,L):
    mo_tmp=list(combinations(mo_lst,i))
    ja_tmp=list(combinations(ja_lst,L-i))
    for j in mo_tmp:
        a=list(j)
        for k in ja_tmp:
            b=list(k)
            tmp=a+b
            tmp.sort()
            s=','.join(tmp)
            s.replace(',','')
            total.append(s)

total.sort()
for i in total:
    print(i.replace(',',''))
