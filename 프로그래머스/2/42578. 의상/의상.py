from collections import defaultdict
import functools
import operator

def solution(clothes):
    answer = 0
    
    category = defaultdict(int)
    for a,b in clothes:
        category[b] += 1
    answer = list(category.values())
    if len(category)==1:
        return answer[0]
    else:
        answer = [count + 1 for count in category.values()]
        return functools.reduce(operator.mul, answer, 1)-1
