def solution(x):
    n = sum([int(c) for c in str(x)])
    return True if x % n == 0 else False