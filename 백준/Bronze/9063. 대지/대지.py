n = int(input())
x=[]
y=[]
for i in range(n):
    a,b= map(int,input().split())
    x.append(a)
    y.append(b)

minx=min(x)
maxx=max(x)

miny=min(y)
maxy=max(y)

print((maxx-minx)*(maxy-miny))
