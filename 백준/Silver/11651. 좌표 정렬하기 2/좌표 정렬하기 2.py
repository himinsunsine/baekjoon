import sys
input = sys.stdin.readline

n = int(input())
points = []

for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))


points.sort(key=lambda point: (point[1], point[0]))

for x, y in points:
    print(x, y)
