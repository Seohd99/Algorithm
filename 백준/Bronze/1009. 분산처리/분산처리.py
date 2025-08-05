import sys
input = sys.stdin.readline

t = int(input())

def solution(a, b):
    c = a % 10
    for _ in range(b-1):
        c = (c * a) % 10
    if c == 0:
        return 10
    return c
for i in range(t):
    a, b = map(int,input().split())
    print(solution(a, b))
