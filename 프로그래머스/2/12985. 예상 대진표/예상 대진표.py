def solution(n,a,b):
    t = 1
    c = 0 
    while(t != n):
        t *= 2
        c += 1
    a = a + 2 ** c - 1
    b = b + 2 ** c - 1
    c = 0
    while(a != b):
        c += 1
        a //= 2
        b //= 2 
    return c