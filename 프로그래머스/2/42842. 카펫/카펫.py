import math
def solution(brown, yellow):
    
    tile = brown + yellow
    
    answer = []
    for i in range(3, int(math.sqrt(tile))+1):
        if tile % i == 0 :
            answer.append(i)
            answer.append(tile//i)
    answer = list(set(answer))
    answer.sort()    
    result = []
    for i in range(len(answer)//2+1):
        if (answer[i]-2) * (answer[-i-1]-2) == yellow :
            result.append(answer[i])
            result.append(answer[-i-1])
    result = list(set(result))
    result.sort(reverse=True)
    if len(result) == 1:
        return result*2
    return result