a,b = map(int, input().split())

def GCD(X,Y):
    while(Y):
        X,Y=Y,X%Y
    return X
result = (a*b)//GCD(a,b)
print(result)
