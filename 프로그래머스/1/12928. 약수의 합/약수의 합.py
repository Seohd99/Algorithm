def solution(n):
    answer = 0
    i = 1

    while i * i <= n:
        if n % i == 0:
            answer += (n // i + i) if n // i != i else i
        i += 1
    return answer