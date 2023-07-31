a,b = map(int,input().split())
c,d = map(int,input().split())
e,f = map(int,input().split())

x = []
x.append(a)
x.append(c)
x.append(e)
y=[]
y.append(b)
y.append(d)
y.append(f)

for i in range(len(x)):
    if x.count(x[i])!=2:
        w=x[i]
        break
for i in range(len(y)):
    if y.count(y[i])!=2:
        z=y[i]
        break

print(w,z)
        
        
        
