n = int(input())

found = False

for i in range(1, n):
    sum_digits = i + sum(int(digit) for digit in str(i))
    if sum_digits == n:
        found = True
        print(i)
        break

if not found:
    print(0)
