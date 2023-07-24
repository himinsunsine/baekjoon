a = input()
a = a.upper()
dic = {}
for i in range(65,91):
    dic[chr(i)]=a.count(chr(i))


maxa = [k for k,v in dic.items() if max(dic.values()) == v]



if len(maxa)>=2:
    print('?')
else:
    print(maxa[0])
    
