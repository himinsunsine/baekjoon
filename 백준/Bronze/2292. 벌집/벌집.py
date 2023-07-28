n = int(input())

s = 1
i = 0

while True:

    s+=6*i
    
    if s>=n:
        break
    i+=1
    
print(i+1)