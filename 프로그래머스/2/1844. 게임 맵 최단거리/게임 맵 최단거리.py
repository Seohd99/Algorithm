from collections import deque
def solution(maps):
    q = deque()
    q.append([0,0,1])
    nx = [-1, 1, 0, 0]
    ny = [0, 0, -1, 1]
    r = len(maps)
    c = len(maps[0])
    ck = [[0 for _ in range(c)]for _ in range(r)]
    ck[0][0] = 1
    while q:
        y, x, t = q.popleft()
        if y+1 == r and x+1 == c:
            return t
        for i in range(4):
            nyp = y + ny[i]
            nxp = x + nx[i]
            if 0 <= nyp and nyp < r and 0 <= nxp and nxp < c and maps[nyp][nxp] == 1 and ck[nyp][nxp] == 0:
                q.append([nyp, nxp, t+1])
                ck[nyp][nxp] = 1
        
    return -1