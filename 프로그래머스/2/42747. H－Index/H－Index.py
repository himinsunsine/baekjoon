def solution(citations):
    citations.sort(reverse = True) # 6 5 3 1 0 / 1 11 111 1111
    answer = 0
    for i in range(len(citations)):
        if citations[i] >= i + 1 :
            answer += 1
    
    return answer