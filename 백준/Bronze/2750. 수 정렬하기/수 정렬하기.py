n = int(input())
a=[]
for i in range(n):
    a.append(int(input()))


for j in range(n-1,0,-1):
    for i in range(0,j,1):
        if (a[i] > a[i + 1]):
            c = a[i + 1]
            a[i + 1] = a[i]
            a[i] = c
for i in range(len(a)):
    print(a[i])