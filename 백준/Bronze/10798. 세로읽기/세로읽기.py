a=[]
for i in range(5):
    a.append(list(input()))

for i in range(15):
    for j in range(5):
        if len(a[j])<i+1:
            continue
        print(a[j][i],end='')

