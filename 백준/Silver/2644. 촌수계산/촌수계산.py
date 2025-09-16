import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int,input().split())
m = int(input())
gragh = [[0 for _ in range(n+1)] for _ in range(n+1)]
CK = [0 for _ in range(n+1)]

def dfs(v,d):
    CK[v] = 1
    if v == b:
        print(d)
        exit()
        
    for i in range(1,n+1):
        if gragh[v][i] == 1 and CK[i] == 0:
            dfs(i,d+1)
    CK[v] = 0
    return 

for i in range(m):
    x, y = map(int,input().split())
    gragh[x][y] = 1
    gragh[y][x] = 1

dfs(a,0)
print(-1)
