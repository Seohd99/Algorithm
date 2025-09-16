import sys
input = sys.stdin.readline

n, m, v = map(int,input().split())
MAP = [[0 for _ in range(n+1)] for _ in range(n+1)]
CK = [0 for _ in range(n+1)]
CK[0] = 1


def dfs(v):
    print(v, end=" ")
    CK[v] = 1
    for i in range(1,n+1):
        if MAP[v][i] == 1 and CK[i] == 0:
            dfs(i)
    return


def bfs(v):
    Q = [v]
    CK[v] = 1
    
    
    for v in Q:
        print(v, end=" ")
        for i in range(1,n+1):
            if MAP[v][i] == 1 and CK[i] == 0:
                Q.append(i)
                CK[i] = 1
    return
for i in range(m):
    x, y = map(int,input().split())
    MAP[x][y] = 1
    MAP[y][x] = 1

dfs(v)
print()
CK = [0 for _ in range(n+1)]
bfs(v)
    
