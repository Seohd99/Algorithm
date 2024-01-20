import sys
sys.setrecursionlimit(10**6)
n = int(input())
MAP = []
for i in range(n):
    MAP.append(list(map(int,input().split())))

nx = [0,0,-1,1]
ny = [-1,1,0,0]
dp = [[0 for i in range(n)]for j in range(n)]

def dfs(x, y):
    if dp[x][y] != 0:
        return dp[x][y]
    for i in range(4):
        nxp = x + nx[i]
        nyp = y + ny[i]
        if nxp >= 0 and nxp < len(MAP) and nyp >= 0 and nyp < len(MAP) and MAP[nxp][nyp] > MAP[x][y]:
            d = dfs(nxp,nyp) + 1
            dp[x][y] = max(d,dp[x][y])
    return dp[x][y]
MAX = 0
for i in range(n):
    for j in range(n):
        MAX = max(MAX,dfs(i,j))

print(MAX+1)
