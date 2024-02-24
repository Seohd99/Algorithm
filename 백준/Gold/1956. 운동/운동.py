import sys

v, e = map(int,sys.stdin.readline().split())
INF = int(1e10)
MAP = [[0 if i == j else INF for i in range(v+1)]for j in range(v+1)]


for i in range(e):
    a, b, c = map(int,sys.stdin.readline().split())
    MAP[a][b] = c

for k in range(1,v+1):
    for i in range(1,v+1):
        for j in range(1,v+1):
            MAP[i][j] = min(MAP[i][j], MAP[i][k]+MAP[k][j])
MIN = INF
for i in range(1,v+1):
    for j in range(i+1,v+1):
        MIN = min(MIN, MAP[i][j] + MAP[j][i])
print(MIN if MIN != INF else -1)