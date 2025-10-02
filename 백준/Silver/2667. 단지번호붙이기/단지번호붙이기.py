import sys
input = sys.stdin.readline
sys.setrecursionlimit(2500)

N = int(input())
MAP = []
nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]

def dfs(y, x):
    cnt = 0
    for i in range(4):
        xx = x + nx[i]
        yy = y + ny[i]
        if 0 <= xx and xx < N and 0 <= yy and yy < N and MAP[yy][xx] == 1:
            MAP[yy][xx] = 0
            cnt += dfs(yy, xx)
    return 1 + cnt
for i in range(N):
    MAP.append(list(map(int, input().strip()))) 
lst = []
C = 0
for y in range(N):
    for x in range(N):
        if MAP[y][x] == 1:
            MAP[y][x] = 0
            C += 1
            lst.append(dfs(y, x))

print(C)
lst.sort()
for i in lst:
    print(i)
