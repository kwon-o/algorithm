import itertools
L,C=map(int,input().split())
il=input().split()
il.sort()
for i in list(itertools.combinations(il,L)):
    ch=len(list(set('aeiou').intersection(i)))
    if ch > 0 and L-ch > 1:
        print("".join(i))