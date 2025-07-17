import sys
sys.setrecursionlimit(30000)  
def countPaths(ny, nx):
    ans = 0
    for i in range(4):
        nxx = nx + xx[i]
        nyy = ny + yy[i]
        if 0 <= nxx and nxx < x and 0 <= nyy and nyy < y and MAP[nyy][nxx] > MAP[ny][nx]:
            if CK[nyy][nxx] == -1:
                ans += countPaths(nyy,nxx)
            else:
                ans += CK[nyy][nxx]
        else:
            ans += 0
    CK[ny][nx] = ans
    return ans

xx = [-1, 1, 0, 0]
yy = [0, 0, -1, 1]

y,x = map(int,input().split())

MAP = []
for i in range(y):
    MAP.append(list(map(int,input().split())))
CK = [[-1 for i in range(x)]for j in range(y)]
CK[0][0] = 1
print(countPaths(y-1,x-1))