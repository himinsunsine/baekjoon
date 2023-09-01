import sys

n, k = map(int, input().split())

a = [i for i in range(1, n + 1)]
lista = []

i = k - 1  # 0부터 시작하는 인덱스
while len(a) >= 1:
    lista.append(a.pop(i))
    if len(a) > 0:
        i = (i + k - 1) % len(a)  # 원형 큐에서 다음 인덱스 계산

print('<', end='')
for i in range(len(lista)):
    if i > 0:
        print(', ', end='')
    print(lista[i], end='')
print('>')
