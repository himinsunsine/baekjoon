H,M = map(int,input().split())
n = int(input())
if (M+n>59):
    H=(M+n)//60 + H
    M=(M+n)%60
    if H>23:
        H=H-24
    print(H,M)
else:
    print(H,M+n)