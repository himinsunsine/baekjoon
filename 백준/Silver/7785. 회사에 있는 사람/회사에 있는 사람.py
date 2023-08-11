n = int(input())

dic={}

for i in range(n):
    x,y = input().split()
    dic[x]=y

dic = sorted(dic.items(), key = lambda item: item[0], reverse = True)

for key,value in dic:
    if value=='enter':
        print(key)
