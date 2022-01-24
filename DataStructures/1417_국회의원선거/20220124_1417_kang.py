import heapq


n = int(input())
num = []


for _ in range(n):
    num.append(int(input()))


count =0
first =0
if n ==1:
    print("0")
else:
    first = num.pop(0)
    #print("first",first)
    while(True):    
        num.sort(reverse=True)
        second = num.pop(0)
       # print("second : ", second)
        if first <= second:
            second -= 1
            first +=1
            num.append(second)
            count +=1
        #    print("first ",first)
        #    print(num)
        if len(num)==0:
            break

        
    print(count)