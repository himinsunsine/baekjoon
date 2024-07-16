def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    
    answer = max(size[0] for size in sizes) * max(size[1] for size in sizes)
    return answer