a=[]
for i in range(9):
    a.append(list(map(int,input().split())))

maxa=0
c=0
b=0

for i in range(9):
    for j in range(9):
        if maxa<a[i][j]:
            maxa=a[i][j]
            c=i
            b=j
print(maxa)
print(c+1,b+1)

