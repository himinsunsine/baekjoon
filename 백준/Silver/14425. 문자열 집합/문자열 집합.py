n,m = map(int, input().split())

listn=set()
listm=[]
count=0

for i in range(n):
    listn.add(input())

for i in range(m):
    listm.append(input())

for i in listm:
    if i in listn:
        count+=1
print(count)