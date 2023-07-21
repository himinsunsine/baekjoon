N = int(input())
score = list(map(int, input().split()))
new = []

M = max(score)
for i in score:
     x = i/M*100
     new.append(x)
total = sum(new)/N

print(total)
