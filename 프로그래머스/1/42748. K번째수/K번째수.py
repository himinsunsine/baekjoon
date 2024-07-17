def solution(array, commands):
    result = []
    for i in range(len(commands)):
        answer = list(array[commands[i][0]-1:commands[i][1]])
        answer.sort()
        result.append(answer[commands[i][2]-1])
    return result