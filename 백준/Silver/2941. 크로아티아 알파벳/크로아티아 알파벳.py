a=input()

b=['c=','c-','dz=','d-','lj','nj','s=','z=']
count=0
for i in range(len(b)):
    if(a.find(b[i])!=-1):
        a = a.replace(b[i],'*')
        count+=1

print(len(a))
    
