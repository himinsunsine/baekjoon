a=[]
for i in range(5):
    a.append(int(input()))


a=sorted(a)


middlea= len(a)//2
print(sum(a)//5)
print(a[middlea])
