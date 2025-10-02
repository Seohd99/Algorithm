import sys
input = sys.stdin.readline
sys.setrecursionlimit(2500)
T = int(input())
nx = [-1, 1, 0 , 0]
ny = [0, 0, -1, 1]

def dfs(y, x):
    for i in range(4):
        xx = x + nx[i]
        yy = y + ny[i]
        if xx >= 0 and xx < m and yy >= 0 and yy < n:
            if MAP[yy][xx] == 1:
                MAP[yy][xx] = 0
                dfs(yy, xx)



for i in range(T):
    m, n, k = map(int,input().split())
    MAP = [[0 for _ in range(m)]for _ in range(n)]
    for i in range(k):
        x, y = map(int,input().split())
        MAP[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if MAP[i][j] == 1:
                MAP[i][j] = 1
                cnt += 1
                dfs(i, j)
    print(cnt)


