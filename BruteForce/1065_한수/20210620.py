from sys import stdin

N = int(stdin.readline()) 
K =[]
count = 0

for i in range(1, N+1) :
    if i <= 99 : # 1부터 99까지는 모두 한수
        count += 1 
    
    else :     
        nums = list(map(int, str(i))) # 숫자를 자릿수대로 분리 
        if nums[0] - nums[1] == nums[1] - nums[2] : #등차수열 확인
            count+=1

print(count)
       


