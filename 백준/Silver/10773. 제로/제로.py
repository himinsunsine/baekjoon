import sys

stack = []

n = int(sys.stdin.readline())


for _ in range(n):
    
    a = int(input())

    if a == 0:
        stack.pop()
    else:
        stack.append(a)

print(sum(stack))