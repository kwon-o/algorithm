
# #11582

import sys
input =sys.stdin.readline

n  = int(input())
misae  = list(map(int,input().split()))
k = int(input())
sorted = [0 for i in range(n)] 

def merge(a,m, middle, n): #리스트 시작점 중간점 끝점
    i =  m 
    j = middle+1
    k = m

    while(i<=middle and j <= n):
        if a[i]<=a[j]:
            sorted[k] = a[i]
            i=i+1
        else:
            sorted[k] = a[j]
            j=j+1
        k=k+1
       
    if i > middle :
        for t in (j,n):
            sorted[k] = a[t]
            k=k+1
    else:
        for t in (i,middle):
            sorted[k] = a[t]
            k =k+1

    return sorted

def mergeSort(a,m,z):
    if m == z :
        return
    middle = int((m+z)/2) #중간값
    mergeSort(a,m,middle)#왼쪽 정렬
    mergeSort(a,middle+1,z) #오른쪽정렬
    merge(a,m,middle,z)


print(mergeSort(misae,0,n-1))



# mid = len(misae)//2
# left = misae[:mid]
# right = misae[mid:]


# while(True):
#     for i in range(int(len(left)/2)):
#         p=i*2
#         #print("left",left[p],left[p+1])
#         if(left[p]>left[p+1]):
#             s = left[p]
#             left[p] =left[p+1]
#             left[p+1] =s
#         #print("right",right[p],right[p+1])
#         if(right[p]>right[p+1]):
#             s = right[p]
#             right[p] =right[p+1]
#             right[p+1] =s
#         #print(left+right)
#     n=n/2
#     if(n==k):
#         break

# print(left+right)


#첫번째 방식


import sys
input =sys.stdin.readline

n  = int(input())
misae  = list(map(int,input().split()))
k = int(input())

buli =[]
ab =0
for i in range(int((len(misae)/2))):
    buli.append(misae[ab:ab+2])
    ab= ab+2

print(buli)

while(True):
    if n == k  or n <k:
        break
    else:
        for i in range(len(buli)):
            buli[i] =sorted(buli[i])

        for i in range(int(len(buli)/2)):
            buli[i] =buli[i]+buli.pop(i+1)
            print(buli[i])
    n = int(n/2)
print(buli)


#두번째  방식
# import sys
# input =sys.stdin.readline

# n  = int(input())
# misae  = list(map(int,input().split()))
# k = int(input())
# buli =[]

# ab =0

# for i in range(int((len(misae)/2))):
#     buli.append(misae[ab:ab+2])
#     ab= ab+2

# while(True):
#     if n == k  or n <k:
#         break
#     else:
#         for i in range(int(len(buli)/2)):
#             buli[i] =sorted(buli[i])
#             buli[i] =buli[i]+sorted(buli.pop(i+1))

#             #print(buli[i])
#     n = int(n/2)
# print(*buli)



