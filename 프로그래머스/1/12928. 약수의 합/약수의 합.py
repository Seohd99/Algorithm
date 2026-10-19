def solution(n):
    answer = 0
    if n == 1 : return 1
    for i in range(1, n//2 + 1):
        t = n//i
        if n % i == 0:
            answer += i
            if t != i : answer += t
        if i + 1 >= t: break

    return answer
