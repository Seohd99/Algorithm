def solution(n):
    answer = [0 if i in [0, 1] else 1 for i in range(n + 1)]
    for i in range(2, n + 1):
        if answer[i] == 0: continue
        if i * i > n:
            break
        answer[i*i:n+1:i] = [0] * len(range(i*i, n + 1, i))
    
    return answer.count(1)