n = int(input())
listn = input().split()

m = int(input())
listm = input().split()

count_dict = {}

for element in listn:
    if element in count_dict:
        count_dict[element] += 1
    else:
        count_dict[element] = 1

answer = []

for i in listm:
    if i in count_dict:
        answer.append(count_dict[i])
    else:
        answer.append(0)

for count in answer:
    print(count, end=' ')