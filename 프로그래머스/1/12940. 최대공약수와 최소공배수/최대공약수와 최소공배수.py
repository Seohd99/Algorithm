def solution(n, m):
    a, b = n, m
    while m:
        t = m
        m = n % m
        n = t
    
    return [ n, a // n * b] 