listA=[]
count=0
for i in range(10):
    listA.append(int(input())%42)
listA=set(listA)
    
print(len(listA))