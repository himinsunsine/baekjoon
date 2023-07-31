x,y,w,h=map(int,input().split())
a=[]

a.append(w-x)
a.append(h-y)
a.append(abs(0-x))
a.append(abs(0-y))

print(min(a))