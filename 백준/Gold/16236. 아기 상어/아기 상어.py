import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
MAP = []
fishes = [0, 0, 0, 0, 0, 0, 0]
result = 0
shark = 2
kill = 2
x , y = -1, -1
nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]
            
for _ in range(N):
    MAP.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        val = MAP[i][j]
        if val == 9:
            y = i
            x = j
            MAP[i][j] = 0
        elif 0 < val <= 6:
            fishes[val] += 1

def bfs():
    queue = deque()
    queue.append([y, x, 0])
    CK = [[0 for _ in range(N)]for _ in range(N)]
    CK[y][x] = 1
    MIN = 400
    my = 20
    mx = 20
    while queue:
        yy , xx, t = queue.popleft()
        if MAP[yy][xx] != 0 and MAP[yy][xx] < shark and MIN >= t:
            if my > yy:
                my = yy
                mx = xx
            elif my == yy:
                if mx > xx:
                    mx = xx
            MIN = t
        if MIN < t:
            return MIN, my, mx

        for i in range(4):
            nyp = yy + ny[i]
            nxp = xx + nx[i]
            if 0 <= nxp and nxp < N and 0 <= nyp and nyp < N and MAP[nyp][nxp] <= shark and CK[nyp][nxp] == 0:
                CK[nyp][nxp] = 1
                queue.append([nyp,nxp,t+1])
    if MIN == 400:
        return 0, -1, -1
    else:
        return MIN, my, mx

            
while sum(fishes[:shark]):
    time, y, x = bfs()
    if time == 0:
        break
    result += time
    MAP[y][x] = 0
    kill -= 1
    if kill == 0:
        shark += 1
        kill = shark

print(result)