def solution(arr):
    
    answer = []

    for x in arr:
        if len(answer) == 0 or answer[-1] != x:
            answer.append(x)
    return answer