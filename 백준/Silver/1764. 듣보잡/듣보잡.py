n,m  = map(int, input().split())

answer={}

for i in range(n):
    x = input()
    answer[x] = 0

count=0 

for i in range(m):
    x = input()
    
    if x in answer:
        answer[x]+=1
        count += 1

   
print(count)

answer=dict(sorted(answer.items()))

for key,i in answer.items():
    if i != 0:
        print(key)
        
