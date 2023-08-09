import sys
input = sys.stdin.readline

n = int(input())
points = []

for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

# x좌표를 기준으로 오름차순 정렬하고, x좌표가 같다면 y좌표를 기준으로 오름차순 정렬합니다.
points.sort(key=lambda point: (point[0], point[1]))

for x, y in points:
    print(x, y)
