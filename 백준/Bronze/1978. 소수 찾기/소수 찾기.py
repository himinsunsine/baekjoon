n = int(input())

arr = list(map(int, input().split(' ')))

num = 0

for i in arr:
    cnt =0
    for j in range(2,i+1):
        if(i%j ==0):
            cnt+=1
    if(cnt==1):
        num +=1
        
print(num)