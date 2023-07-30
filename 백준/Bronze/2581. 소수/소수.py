import math
M = int(input())
N = int(input())        

a = [i for i in range(M,N+1)]

mina=max(a)
result = 0

def prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num%i==0:
            return False
    return True

for i in range(len(a)):
    if prime(a[i]):
        result+=a[i]

        if mina>a[i]:
            mina=a[i]
if result==0:
    print('-1')
else:
    print(result)
    print(mina)

            
        
        
        
