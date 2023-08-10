n = int(input())
group = []

for i in range(n):
    age,name = input().split()
    group.append((int(age),name))


group.sort(key=lambda group:group[0])

for i in group:
    print(i[0],i[1])
