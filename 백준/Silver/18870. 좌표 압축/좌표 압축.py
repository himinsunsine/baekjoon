n = int(input())
group = list(map(int, input().split()))

group2 = sorted(set(group))
group_dict = {val: idx for idx, val in enumerate(group2)}
answer = [group_dict[val] for val in group]

print(*answer)
