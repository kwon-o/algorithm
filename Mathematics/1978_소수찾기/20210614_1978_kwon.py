a=input()
l=list(map(int,input().split()))
ans=0
def isPrime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True
for j in l:
	if(isPrime(j)):
		ans+=1
print(ans)