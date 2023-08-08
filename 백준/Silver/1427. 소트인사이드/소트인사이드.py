n = list(map(int, input()))
array=[]

while True:
    maxn = max(n)
    array.append(maxn)
    n.remove(maxn)
    if len(n)==0:
        break
    
for i in range(len(array)):
    print(array[i],end='')

        
