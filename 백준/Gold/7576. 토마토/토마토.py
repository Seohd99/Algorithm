from collections import deque

x, y = map(int, input().split())
MAP = []
xx = [-1, 1, 0, 0]
yy = [0, 0, -1, 1]

for i in range(y):
    MAP.append(list(map(int, input().split())))

Q = deque()
for i in range(y):
    for j in range(x):
        if MAP[i][j] == 1:
            Q.append((j, i, 0))

ans = 0
while Q:
    nx, ny, d = Q.popleft()
    for i in range(4):
        nxx = nx + xx[i]
        nyy = ny + yy[i]
        if 0 <= nxx < x and 0 <= nyy < y and MAP[nyy][nxx] == 0:
            Q.append((nxx, nyy, d + 1))
            MAP[nyy][nxx] = 1
    ans = max(ans, d)

print(-1 if any(0 in row for row in MAP) else ans)
