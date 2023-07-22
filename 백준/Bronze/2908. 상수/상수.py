a, b = input().split()

newa = ''.join(a[-i] for i in range(1, 4))
newb = ''.join(b[-i] for i in range(1, 4))

newa = int(newa)
newb = int(newb)

print(newa if newa > newb else newb)
