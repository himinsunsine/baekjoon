N ,M = map(int,input().split())
a = list(map(int,input().split()))

from itertools import combinations

answer=[]

for i in combinations(a, 3):
    if sum(i) <= M:
         answer.append(sum(i))
answer = list(set(answer))
print(max(answer))