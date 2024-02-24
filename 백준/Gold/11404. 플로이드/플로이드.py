n = int(input())
m = int(input())
nodes = []
INF = int(1e14)
MAP = [[INF if i != j else 0 for i in range(n+1)]for j in range(n+1)]


for i in range(m):
    a, b, c = map(int,input().split())
    MAP[a][b] = min(MAP[a][b],c) 

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            MAP[j][k] = min(MAP[j][k], MAP[j][i]+MAP[i][k])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(MAP[i][j] if MAP[i][j]!= INF else 0,end=" ")
    print()




