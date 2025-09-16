import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000)
n = int(input())
m = int(input())
gragh = [[0 for _ in range(n+1)]for _ in range(n+1)]
CK = [0 for _ in range(n+1)]


def dfs(v):
    CK[v] = 1
    cnt = 0
    for i in range(1,n+1):
        if gragh[v][i] == 1 and CK[i] == 0:
            cnt += dfs(i)
    return 1 + cnt
    
for _ in range(m):
    x, y = map(int,input().split())
    gragh[x][y] = 1
    gragh[y][x] = 1

print(dfs(1) - 1)