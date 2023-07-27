a ="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c=""

N, B = map(int,input().split())
while True:
    c+=(str(a[N % B]))
        
    N //= B
    
    if N == 0:
        break
    
print(c[::-1])
