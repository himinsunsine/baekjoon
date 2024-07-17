def solution(arr):
    queue = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    queue.append(arr[0])
    for i in arr[1:]:
        top = queue[-1]
        if i != top:
            queue.append(i)

    
    return queue