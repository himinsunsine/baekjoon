total = int(input())
n = int(input())
sum=0

for i in range(0,n):
    A,B=map(int,input().split())
    sum = sum + A * B

if(sum==total):
    print("Yes")
else :
    print("No")