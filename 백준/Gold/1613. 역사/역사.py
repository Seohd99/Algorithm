import sys
n , m = map(int,sys.stdin.readline().split())
INF = int(1e10)
his = [[0 if i == j else INF for i in range(n+1)]for j in range(n+1)]

for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    his[a][b] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):  
            his[i][j] = min(his[i][j],his[i][k]+his[k][j])


s = int(sys.stdin.readline())
for i in range(s):
    a, b = map(int,sys.stdin.readline().split())
    if his[a][b] != INF:
        print(-1)
    elif his[b][a] != INF:
        print(1)
    else:
        print(0)
 