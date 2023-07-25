a, b = map(int, input().split())

arr = []
arr2 = []
brr = [[0 for _ in range(b)] for _ in range(a)]

for i in range(a):
    arr.append(list(map(int, input().split())))
    
for i in range(a):
    arr2.append(list(map(int, input().split())))

for i in range(a):
    for j in range(b):
        brr[i][j] = arr[i][j] + arr2[i][j]

for k in brr:
    print(*k)
