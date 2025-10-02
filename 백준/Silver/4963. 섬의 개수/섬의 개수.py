import sys
sys.setrecursionlimit(2500)
input = sys.stdin.readline

nx = [-1, 1, 0, 0, 1, 1, -1, -1]
ny = [0, 0, -1, 1, 1, -1, -1, 1]

def dfs(y, x):
    for i in range(8):
        xx = x + nx[i]
        yy = y + ny[i]
        if 0 <= xx and xx < w and 0 <= yy and yy < h and MAP[yy][xx] == 1:
            MAP[yy][xx] = 0
            dfs(yy, xx)
    
while(True):
    w, h = map(int,input().split())
    if w + h == 0:
        break
    MAP = []
    for i in range(h):
        MAP.append(list(map(int,input().split())))

    cnt = 0
    for y in range(h):
        for x in range(w):
            if MAP[y][x] == 1:
                cnt += 1
                MAP[y][x] = 0
                dfs(y, x)
    print(cnt)
