N,M=map(int,input().split())
listA=[i for i in range(1,N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    r=b-a+1
    for _ in range(r//2):
        listA[a-1],listA[b-1]=listA[b-1],listA[a-1]
        a+=1
        b-=1
for i in range(N):
    print(listA[i],end=' ')