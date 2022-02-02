N = int(input())

dan =[]
for i in range(N):              
    dan.append(input())               
 
list1 = list(set(dan))       
 
list2 = []
 
for j in list1:
    list2.append((len(j), j))      
 
list2.sort()                      
 
for len_a,a  in list2:       
    print(a)