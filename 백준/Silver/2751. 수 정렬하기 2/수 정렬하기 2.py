import sys
input=sys.stdin.readline

n = int(input())

a=[]
for i in range(n):
    a.append(int(input()))

a=sorted(a)

print(*a)
