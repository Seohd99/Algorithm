def solution(n):
    x = 1
    answer = -1
    while x * x <= n:
        if x * x == n:
            answer = (x + 1) ** 2
            break
        x += 1
    return answer