n, b = input().split()
b = int(b)
t = 0

alpha = [chr(a) for a in range(65, 91)]


for i in range(len(n)):
    if n[i] in alpha:
        t += (ord(n[i]) - 55) * (b**(len(n) - i - 1))
    else:
        t += (ord(n[i]) - 48) * (b**(len(n) - i - 1))

print(t)