import sys
sys.setrecursionlimit(3000)
input = sys.stdin.readline

n, m = map(int,input().split())
CK = [0 for _ in range(n+1)]
CK[0] = 1
cnt = 0 
MAP = [[0 for _ in range(n+1)] for _ in range(n+1)]

def dfs(v):
    CK[v] = 1
    for i in range(1,n+1):
        if MAP[v][i] == 1 and CK[i] == 0:
            dfs(i)
    return


for i in range(m):
    x, y  = map(int,input().split())
    MAP[x][y] = 1
    MAP[y][x] = 1

for i in range(1, n + 1):
    if CK[i] == 0:
        cnt += 1
        dfs(i)
print(cnt)