#킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
lista=input().split()
listb = [1,1,2,2,2,8]

for i in range(6):
    if(int(lista[i])!=listb[i]):
        print(listb[i]-int(lista[i]),end=' ')
    else:
        print('0',end=' ')
