def solution(n):
    answer = 0
    i = 1

    while i * i <= n:
        if n % i == 0:
            x = n // i
            answer += (x + i) if x != i else i
        i += 1
    return answer